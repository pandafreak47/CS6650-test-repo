<file path="tests/test_models.py">
from unittest import TestCase
from unittest.mock import Mock

from .order import Order
from .user import User


class TestModel(TestCase):
    
     def setUp(self) -> None:
         Mock(UserWithToken).return_value = Mock()
         Mock(UserWithPassword).return_value = Mock()
        
     def test_display(self):
         order = Order(id=1, user=User(username="user1"), items=["a", "b", "c"], total=100.0)
         self.assertEqual(order.display(), f"Order(1, User(username='user1'), items=[a, b, c], total=100.0)")
         order = Order(id=2, user=User(username="user2"), items=["a", "b", "c"], total=100.0)
         self.assertEqual(order.display(), f"Order(2, User(username='user2'), items=[a, b, c], total=100.0)")
         with self.assertRaises(ValueError):
             Order(id=3, user=User(username="user3"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=4, user=User(username="user4"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=5, user=User(username="user5"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=6, user=User(username="user6"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=7, user=User(username="user7"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=8, user=User(username="user8"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=9, user=User(username="user9"), items=["a", "b", "c"], total=100.0)
         with self.assertRaises(ValueError):
             Order(id=10, user=User(username="user10"), items=["a", "b", "c"], total=100.0)

     def test_display_with_user(self):
         order = Order(id=1, user=User(username="user1"), items=["a", "b", "c"], total=100.0)
         self.assertEqual(order.display(), f"Order({order.id}, User(username='user1'), items=[a, b, c], total=100.0)")
         with self.assertRaises(ValueError):
             Order(id=11, user=User(username="user1"), items=["a", "b", "c"], total=100.0)

     def test_display(self):
         order = Order(id=1, id2, "user", "email", hash=hash)
         self.assertEqual(fidict, "Email",fidict[1,items=[a,b]
            order = fignot[1,email]
        password_a[1,email,b,email/hash,email,hash,email,items,email,email,email,b,email,email,email
class,email,email[email, f,hash, username=email,email,f,email,email, email,email,email,email,email,email
email,email,email,email,email,email,f,email,f,email,email,email,email,email,email,email,email,email,email,email,email, email,email,email,email,email,email,email,email,email,email,email,email
email,email,email,email,email,email,email,email,email