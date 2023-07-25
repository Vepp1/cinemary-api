# Cinemary - API

Backend application built using Django REST that allows account, posts, comments, and likes creation. The API is consumed by the front-end application Cinemary. All models are validated with REST framework serializers.

---

## Models

### Profiles

- owner - Foreign Key from Django auth User.
- name - Character field with a max length of 50.
- created_at - Datetime field set automatically when a profile is created.
- updated_at - Datetime field set automatically when a profile is updated.

### Posts

- owner - Foreign Key from Django auth User.
- created_at - Datetime field set automatically when a post is created.
- updated_at - Datetime field set automatically when a post is updated.
- title - Character field with a max length of 50.
- genre - Character field with a max length of 25.
- actors - Character field with a max length of 100.
- director - Character field with a max length of 50.
- content - Text field.
- image - Image field.

### Likes

- owner - Foreign Key from Django auth User.
- post - Foreign Key from Posts module.
- created_at - Datetime field set automatically when like is created.

### Comments

- owner - Foreign Key from Django auth User.
- post - Foreign Key from Posts module.
- created_at - Datetime field set automatically when a comment is created.
- updated_at - Datetime field set automatically when a comment is created.
- content - Text field.

---

## Testing and Validation

### Manual Testing

### Create post being logged out.

- Access /posts and try to create post.
- Result: Create post functionality is not available to logged out users.

### Edit or delete posts user or being logged out.

- Access a post through the address bar using the /posts/'id' or /comments/'id' and try to delete or edit it.
- Result: The page is going to be a Read-Only, due to permission classes.

### Create or edit a post with an image of an invalid format.

- After logging into an account, access /post and try to create a review with an image that is not a jpeg file.
- Result: Error will be displayed and a post will not be created.

### Create or edit a post with fields with more than 50 characters.

- After logging into an account try to to add a post with an exceptionally long title, genre or director.
- Result: Error will be displayed and a post will not be created.

### Like a Post without being logged in.

- Access /likes and try to like one of the existing posts.
- Result: Like functionality is not available to logged out users.

### Like same post twice.

- Access /likes and try to like one post you previously liked.
- Result: Message displayed saying that duplicate is not allowed.

### Delete like made by another user.

- Access the like detail page /likes/'like_id' and try to delete it.
- Result: The page is going to be a Read-Only, due to permission classes.

### Create comment being logged out.

- Access /comments and try to create comment on a existing post.
- Result: Create comment functionality is not available to logged out users.

### Edit or delete comments from another user.

- Access a comment through the address bar using /comments/'id' and try to delete or edit it.
- Result: The page is going to be a Read-Only, due to permission classes.

### Verify response payload and status code.

- Result: All JSON responses are sending correct field names, types and values. Permited requests are returning 200 status and unpermitted 400.

### Verify basic performance

- Result: All operations are being completed in a reasonable amount of time.

### Validator Testing

- PEP8
  - All pages passed through vs code python linter.

### Unfixed Bugs

There are no present bugs in this version.

---

## Deployment

- The live link can be found [here](https://cinemary-api.herokuapp.com/).
- [GitHub Repo](https://github.com/Vepp1/cinemary-api).

### Heroku

- Deploying to Heroku:
  - Access www.heroku.com.
  - Click on new and Create New App.
  - Choose an App name and a region and Create App.
  - Acces Settings tab.
  - Set the config vars to connect to database, cloudinary and allowed host.
  - On the Deployment tab, connect to Github and choose the proper repository.
  - Deploy Branch.

### GitHub/GitPod

- Forking the GitHub Repository:

  - If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.
  - Find the relevant GitHub repository
  - In the top right corner of the page, click the Fork button (under your account)
  - Your repository has now been 'Forked' and you have a copy to work on
  - Cloning the GitHub Repository

- Cloning your repository will allow you to download a local version of the repository to be worked on.

  - Find the relevant GitHub repository.
  - Press the arrow on the Code button.
  - Copy the link that is shown in the drop-down.
  - Now open Gitpod & select the directory location where you would like the clone created.

  - In the terminal type 'git clone & then paste the link you copied in GitHub. - Press enter and your local clone will be created.

  ### Front End

  - To connect with Front End application:

    - Add the frontend url to CORS_ALLOWED_ORIGINS and CLIENT_ORIGIN.
    - Retrieve reviews with GET cinemary-api.herokuapp.com/posts. 
    - Create, update or delete reviews with POST, PUT, DELETE /posts/{post_id}
    - Retrieve comments with GET cinemary-api.herokuapp.com/comments. 
    - Create, update or delete coments with POST, PUT, DELETE /comments/{comment_id}
    - Retrieve likes with GET cinemary-api.herokuapp.com/likes. 
    - Create or delete likes with POST, PUT /likes/{like_id}
    - Signup requests must be sent to cinemary-api.herokuapp.com/dj-rest-auth/registration/ with POST.
    - Signin requests must be sent to cinemary-api.herokuapp.com/dj-rest-auth/login/ with POST.
    - Logout requests must be sent to cinemary-api.herokuapp.com/dj-rest-auth/logout/ with POST.
    - Password change requests must be sent to cinemary-api.herokuapp.com/dj-rest-auth/password/change/ with POST.
    - Username change requests must be sent to cinemary-api.herokuapp.com/dj-rest-auth/user/ with POST.
    

---
