import os

class review:
    
    def __init__(self):
        self.review_filename = None
        self.review_label = None
        self.original_review = None
        self.process_review = None

    def load_review(self, movie_review_folder, data_type, review_type, review_filename):
        with open(os.path.join(movie_review_folder, "aclImdb", data_type, review_type, review_filename), 'r') as file:
            text_review = file.read()
        
        self.review_filename = review_filename
        self.review_label = review_type
        self.original_review = text_review

    def __str__(self):
        return f"FILE: {self.review_filename}\nLABEL: {self.review_label}\nORIGINAL: {self.original_review}"