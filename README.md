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
- genre - Character field with a max length of 50.
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

### Edit or delete posts/comments from another user or being logged out.

- Access a post or comment through the address bar using the /posts/'id' or /comments/'id' and try to delete or edit it.
- Result: The page is going to be a Read-Only, due to permission classes.

### Create or edit a post with an image of an invalid format.

- After logging into an account, access /post and try to create a review with an image that is not a jpeg file.
- Result: Error will be displayed and a post will not be created.

### Create or edit a post with a title or genre with more than 50 characters.

- After logging into an account try to access go to create and try to add a post with an exceptionally long title or genre.
- Result: Error will be displayed and a post will not be created.

### Validator Testing

- PEP8
  - All pages passed through vs code python linter.

### Unfixed Bugs

There are no present bugs in this version.

---

## Deployment

- The live link can be found [here](https://vegancaju.herokuapp.com/).
- [GitHub Repo](https://github.com/Vepp1/cinemary).

#### GitHub/GitPod

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

---
