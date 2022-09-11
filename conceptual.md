### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python is mainly used for backend development and is great for use with things that involve data science or AI and machine learning.

  JS can be used for front end or backend development and is commonly used in app development.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  get(key,val)

  setdefault(key, val)


- What is a unit test?

  A unit test is a test that checks an individual component of the code.


- What is an integration test?

  An integration test checks to see if the parts of the code work together properly.


- What is the role of web application framework, like Flask?

  Frameworks provide existing libraries and tools to help accomplish various goals within web development.


- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?

  You would choose based on whether you're attempting to filter resources (?/=) or directly using a resource ID in the URL (/). 
  

- How do you collect data from a URL placeholder parameter using Flask?

  request.args.get("key")


- How do you collect data from the query string using Flask?

  request.args


- How do you collect data from the body of the request using Flask?

  request.data


- What is a cookie and what kinds of things are they commonly used for?

A cookie is a way to store a small amount of information on a browser. It is a string/value pair. 


- What is the session object in Flask?

The session object can be used/treated as  dictionary which allows us to access session directly. Sessions are stored as a cookie.


- What does Flask's `jsonify()` do?

This allows us to not write JSON by hand as it can be hard to format correctly, rather this will render a json response object for us. 
