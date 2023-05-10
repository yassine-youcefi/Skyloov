import os 
import pytest
from PIL import Image
from io import BytesIO
from datetime import datetime
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
class TestProductsFilter:
    """
        - Test the products search 'filter' endpoint by sending a GET request to the endpoint with different search criteria,
        and ensuring that the correct list of matching products is returned in the response after providing a valid JWT token.
        - Test the implementation by uploading test images and verifying that the correct resized images are generated and stored.
    """

    def test_search_products_unauthorized_users(self, unknown_client):
        """
          Test unauthorized user case
          assertions :
            - status code = 401.
            - error meessage.
        """

        url = reverse("products-search")
        response = unknown_client.get(f"{url}?name=test")
        assert response.status_code == 401
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    def test_search_products_404_not_found(self, client):
        """
          Test search with not found results
          assertions :
            - status code = 404.
            - error meessage.
        """

        url = reverse("products-search")
        response = client.get(f"{url}?name=test 404")
        assert response.status_code == 404
        assert response.data['detail'] == 'No results found for the requested page'

    def test_search_products_by_name(self, client, product):
        """
          Test search for a product by its name. It uses the client and product fixtures
          assertions :
            - status code.
            - response data count.
            - the returned product brand name.
        """

        url = reverse("products-search")
        product_name = 'test product'
        response = client.get(f"{url}?name={product_name}")
        assert response.status_code == 200
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == product_name

    def test_search_products_by_brand(self, client, product):
        """
          Test search for a product by its brand name.
          assertions :
            - status code.
            - the returned product brand name
        """

        url = reverse("products-search")
        brand_name = 'test brand'
        response = client.get(f"{url}?brand={brand_name}")
        assert response.status_code == 200
        assert response.data['results'][0]['brand'] == brand_name

    def test_search_products_by_category(self, client, product):
        """
          Test search for a product by its category name.
          assertions :
            - status code.
            - the returned product brand name
        """

        url = reverse("products-search")
        category_name = "test category"
        response = client.get(f"{url}?category={category_name}")
        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["category"] == category_name

    def test_search_products_by_price(self, client, product):
        """
          Test search for a product by price range.
          assertions :
            - status code.
            - the returned product price must be includes in the price range
        """

        url = reverse("products-search")
        min_price = 0
        max_price = 100
        response = client.get(
            f"{url}?min_price={min_price}&max_price={max_price}")
        assert response.status_code == 200
        assert float(response.data['results'][0]['price']) >= min_price
        assert float(response.data['results'][0]['price']) <= max_price

    def test_search_products_by_quantity(self, client, product):
        """
          Test search for a product by quantity range.
          assertions :
            - status code.
            - the returned product quantity must be includes in the quantity range
        """

        url = reverse("products-search")
        min_quantity = 0
        max_quantity = 5
        response = client.get(
            f"{url}?min_quantity={min_quantity}&max_quantity={max_quantity}")
        assert response.status_code == 200
        assert response.data['results'][0]['quantity'] >= min_quantity
        assert response.data['results'][0]['quantity'] <= max_quantity

    def test_search_products_by_rating(self, client, product):
        """
          Test search for a product by rating.
          assertions :
            - status code.
            - the returned product rating must be exact
        """

        url = reverse("products-search")
        rating = 4.5
        response = client.get(f"{url}?rating={rating}")
        assert response.status_code == 200
        assert float(response.data['results'][0]['rating']) == rating

    def test_search_products_by_created_at(self, client, product):
        """
              Test search for a product by rating. 
              assertions : 
                - status code.
                - the returned product created_at date must be exact
            """

        url = reverse("products-search")
        created_at = datetime.now().strftime('%Y/%m/%d')
        response = client.get(f"{url}?created_at={created_at}")
        assert response.status_code == 200
        assert response.data['results'][0]['created_at'] == created_at

    def test_put_product_image(self, client, product):
        """
          Test update product image. 
          assertions : 
            - status code.
            - products images validation (by file name)
        """
        url = reverse("product_image_upload", kwargs={'pk': product.id})
        with open('email.png', 'rb') as f:
            image = SimpleUploadedFile(
                name='image.png', content=f.read(), content_type='image/png')

        response = client.put(f"{url}",  {'image': image})
        
        assert response.status_code == 200


        product.refresh_from_db()

        assert response.json()['success'] == 'Image uploaded successfully'
        assert product.image.name.split('/')[1] is not None
        assert product.image_thumbnail.name.split('/')[1] is not None
        
        os.remove(product.image.path)
        os.remove(product.image_thumbnail.path)
