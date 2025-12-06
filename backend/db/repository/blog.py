from sqlalchemy.orm import Session
from db.models.blog import Blog
from schemas.blog import BlogCreate, UpdateBlog

def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    
    blog = Blog(
        title = blog.title,
        slug = blog.slug,
        content = blog.content,
        author_id = author_id
    )
    
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_blog_by_id(id: int, db:Session):
    return db.query(Blog).filter(Blog.id == id).first()


def get_all_blogs(db: Session):
    return db.query(Blog).filter(Blog.is_active==True).all()

def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    blog_in_db = db.query(Blog).filter(Blog.id==id).first()
    if not blog_in_db:
        return {"error": f"Blog with id {id} doesn't exist"}
    if not blog_in_db.author_id == author_id:
        return {"error": f"Only the author can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    blog_in_db.slug = blog.slug
    db.add(blog_in_db)
    db.commit()
    return blog_in_db 


def delete_blog_by_id(id: int, db: Session, author_id: int):
    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog:
        return {"error": f"Could not find blog with id {id}"}
    if not blog.author_id == author_id:
        return {"error": f"Only the author can delete a blog"}
    
    #blog.delete() also works
    db.delete(blog)
    db.commit()
    return {"msg": f"Deleted blog with id {id}"}



