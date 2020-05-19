import unittest
from app import db
from model import User,Post,Comment

class UserTest(unittest.TestCase):

    def setUp(self):

        self.new_user = User(password='leilanjeri')

    def test__passoword_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def setUp(self):
        self.user_lorraine = User(username = 'lorraine',password = 'lorra', email = 'lorra@.gmailom',image_file = "profile.jpg")
        self.new_post= Post(user_id = 1,post_id =1,title='Insiprational',content="i am hebrew",date = "2021/5/6",user = self.user_lorraine )
        self.new_comment= Comment(comment_id =1,post_id=1,post_title='Insiprational',comment = "bool",user = self.user_lorraine )
    """
    checking class instantiation
    """
    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.post_id,1)
        self.assertEquals(self.new_post.role_title,'Inspirational')
        self.assertEquals(self.new_post.image_file,"profile.jpg")
        self.assertEquals(self.new_post.new_comment,'bool')
        self.assertEquals(self.new_post.user,self.user_lorraine)
