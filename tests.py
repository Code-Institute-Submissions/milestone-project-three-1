import app
import unittest

class UnitTests(unittest.TestCase):
    
    def create_app(self):
        return app
        
    # def test_index_page(self):
    #     self.app.get('/')
    #     self.assert_template_used('index.html')

    # def test_questions_page(self):
    #     self.app.get('/')
    #     self.assert_template_used('questions.html')

    # def test_success_page(self):
    #     self.app.get('/')
    #     self.assert_template_used('success.html')

      
    def test_get_a_question(self):
        self.assertEqual(app.get_question(1), "{'question': 'The more you take, the more you leave behind. What am I?', 'answer':'Footsteps'}")
        

        
        
if __name__ == '__main__':
    unittest.main()