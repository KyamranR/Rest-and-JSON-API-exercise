from unittest import TestCase
from flask import current_app
from app import app
from models import db, Cupcake

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True




CUPCAKE_DATA = {
    "flavor": "TestFlavor",
    "size": "TestSize",
    "rating": 5,
    "image": "http://test.com/cupcake.jpg"
}

CUPCAKE_DATA_2 = {
    "flavor": "TestFlavor2",
    "size": "TestSize2",
    "rating": 10,
    "image": "http://test.com/cupcake2.jpg"
}


class CupcakeViewsTestCase(TestCase):
    """Tests for views of API."""

    def setUp(self):
        """Make demo data."""

        self.app_context = app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

        cupcake = Cupcake(**CUPCAKE_DATA)
        db.session.add(cupcake)
        db.session.commit()

        self.cupcake = cupcake

    def tearDown(self):
        """Clean up fouled transactions."""

        db.session.rollback()

        self.app_context.pop()

    def test_list_cupcakes(self):
        with app.test_client() as client:
            resp = client.get("/api/cupcakes")

            self.assertEqual(resp.status_code, 200)

            data = resp.json
            self.assertEqual(data, {
                "cupcakes": [
                    {
                        "id": self.cupcake.id,
                        "flavor": "TestFlavor",
                        "size": "TestSize",
                        "rating": 5,
                        "image": "http://test.com/cupcake.jpg"
                    }
                ]
            })

    def test_get_cupcake(self):
        with app.test_client() as client:
            url = f"/api/cupcakes/{self.cupcake.id}"
            resp = client.get(url)

            self.assertEqual(resp.status_code, 200)
            data = resp.json
            self.assertEqual(data, {
                "cupcake": {
                    "id": self.cupcake.id,
                    "flavor": "TestFlavor",
                    "size": "TestSize",
                    "rating": 5,
                    "image": "http://test.com/cupcake.jpg"
                }
            })

    def test_create_cupcake(self):
        with app.test_client() as client:
            url = "/api/cupcakes"
            resp = client.post(url, json=CUPCAKE_DATA_2)

            self.assertEqual(resp.status_code, 201)

            data = resp.json

            self.assertIn('message', data)
            self.assertEqual(data['message'], 'Cupcake created!')
            
            self.assertEqual(Cupcake.query.count(), 2)

            new_cupcake = Cupcake.query.filter_by(flavor='TestFlavor2').first()

            self.assertIsNotNone(new_cupcake)
            self.assertIsInstance(new_cupcake.id, int)

def test_update_cupcake(self):
    with app.test_client() as client:
        url = f'/api/cupcakes/{self.cupcake.id}'
        resp = client.patch(url, json={'flavor': 'UpdatedFlavor'})

        self.assertEqual(resp.status_code, 200)

        data = resp.json
        self.assertIn('cupcake', data)
        self.assertEqual(data['cupcake']['flavor'], 'UpdatedFlavor')

        updated_cupcake = Cupcake.query.get(self.cupcake.id)
        self.assertEqual(updated_cupcake.flavor, 'UpdatedFlavor')


def test_delete_cupcake(self):
    with app.test_client() as client:
        url = f'/api/cupcakes/{self.cupcake.id}'
        resp = client.delete(url)

        self.assertEqual(resp.status_code, 200)

        data = resp.json
        self.assertIn('message',data)
        self.assertEqual(data['message'], 'Cupcake deleted!')

        deleted_cupcake = Cupcake.query.get(self.cupcake.id)
        self.assertIsNone(deleted_cupcake)