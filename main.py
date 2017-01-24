import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        #a dropdown to cross off movies
        crossoff_form = """
        <form action="/cross-off" method="post">
            <select name="remove-movie">
                <option value="Napoleon Dynamite">Napoleon Dynamite</option>
                <option value="American Beauty">American Beauty</option>
                <option value="Life Is Beautiful">Life Is Beautiful</option>
                <option value="Mulan">Mulan</option>
            </select>
            <input type="submit" value="Remove It"/>
        </form>
        """

        content = page_header + edit_header + add_form + "<br>" + crossoff_form + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


class RemoveMovie(webapp2.RequestHandler):
    """Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross
    """
    def post(self):
        #read in request to find out what the user typed
        remove_movie = self.request.get("remove-movie")

        #build response content
        remove_movie_element = "<strong>" + remove_movie + "</strong>"
        sentence = remove_movie_element + " has been crossed off your watchlist."

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', RemoveMovie)
], debug=True)
