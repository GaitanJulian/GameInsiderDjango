# GAME INSIDER
#### Video Demo:  <URL HERE>
#### Description: The following project is a page to publish forums about video games, users can search for posts about their favorite videos, like and comment on the posts they want. Users can also edit their own profile, and log in to see in an orderly fashion all the posts they have made. The project was made using the django framework.

## Models
Let's start by reviewing all the models created.


### Author
The author models refers to every user in the webpage, the model includes data as for example their full name or their profile picture.

### Game
This model refers to a Game that is possible to create a post about.

### Post, Like, Comment
This models refers to a publication that a user can make, i also created some other models to save the users likes and commentaries.


## Templates
Nos lets review some of the templates that we have for rendering the page.

### Registration

#### Bio.html
This html is rendered when a user wants to update any old information about himself.

#### Signin.html
An html that is rendered when a user wants to sign in to the webpage with an already created account

#### Signup.html
Similar to the previous one, this html is rendered when a user wants to create a new account.

#### Update.html
This html is pretty similar to the Bio.html and maybe i could only have one, but i decided to have theese two, this html is immediatily rendered after the user created a new account, in order to update the Author biography, their full name and the profile picture.

### Base.html
I should have started with this template, this is the base html for rendering all the other templates in the website, this html contains the navbar of the pages as well as some references for example to bootstrap. Every other template in the page inhherits from this template.

### Home.html
The Homepage of the website, counts with a centered search bar where users can search any post or content in the website. Just below the searchbar there is one carousel of popular games that users can find posts about

### Search.html
This is the html that is rendered when a user search any keyword, it display in columns of three post available.

### post_detail.html
This is the html that is rendered when a user clicks on a post to open it completely, it shows the thumbnail of the post as well as every important information. Here users can like the posts or make their own comments.

### create_post.html
This renders a form that allows the user to create a new publication.

### add_comment.html
This is a small form that is loaded inside the post_detail.html, this is the form that allows user to publicate any new comment.