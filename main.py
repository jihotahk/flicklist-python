import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movies = ["Princess Bride", "The Departed", "Mulan", "Napoleon Dynamite", "Fargo"]
        # TODO: randomly choose one of the movies, and return it
        picked_movie = movies[random.randint(0, len(movies)-1)]

        return picked_movie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        tom_movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tom_content = "<h1>Tomorrow's Movie</h1>"
        tom_content += "<p>" + tom_movie + "</p>"

        self.response.write(content)
        self.response.write(tom_content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
