from django.db import models

# Create your models here.
"""
Author
    - Name - dictionary {First Name: string(50), Last Name:string(50)}
    - Email - {Email: string(50)}
    - Bio - string(5000)
    - Profile Picture - image
    - Slug - string(100)
    - Status - [Active, Inactive]
    - Posts - list of posts
   
Post
    - Title - string(100)
    - Content - text
    - Author - foreign key to Author
    - Date - datetime
    - Last Updated Date - datetime
    - Image1 - Image
    - Image2 - Image
    - Image3 - Image
    - Image4 - Image
    - Category - foreign key to Category
    - Tags - list of tags
    - Slug - string(100)
    - Status - [Draft, Published, Deleted]
    - Featured - boolean
    - Views - integer
    - Likes - integer
    - Comments - list of comments
    - Shares - integer

Commenter
    - Name - string(50)
    - Email - string(50)

Comment
    - Commenter - foreign key to Commenter
    - Comment - string(500)
    - Date - datetime
    - Post - foreign key to Post
    - Status - [Published, Censored, Deleted]
    - Likes - integer
    - Replies - list of comments

Category
    - Name - string(50)
    - Description - string(500)
    - Posts - list of posts

Tag
    - Name - string(50)
    - Description - string(500)
    - Posts - list of posts

stopping at 33:47 on video, moving over to Hackerrank for interview prep for a bit
"""