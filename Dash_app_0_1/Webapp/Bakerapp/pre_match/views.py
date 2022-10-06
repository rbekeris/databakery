from . import pre_match
@pre_match.route('/')
def index(self):
    return self.render('second.html')