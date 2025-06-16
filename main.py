from fastapi import FastAPI, HTTPException
from prisma import Prisma
from prisma.models import User
from pydantic import EmailStr, BaseModel

database = Prisma()
app = FastAPI(
    version="0.1"
)

class UserDto(BaseModel):
    name: str = None
    email: EmailStr = None

class PostDto(BaseModel):
    title: str
    content: str
    author_id: int

@app.get("/healthz")
def test_page():
    return {"condition": "working"}

@app.post("/user/create")
async def create_new_user(userdto: UserDto):
    try:
        await database.connect()
        new_user = await database.user.create(data=userdto.model_dump())
        return {"status": "done", "user": new_user}
    except Exception as e:
        raise HTTPException(500, f"error creating user {e}")
    finally:
        await database.disconnect()


@app.get("/user/{user_id}")
async def get_user_data(user_id: int):
    try:
        await database.connect()
        user_data = await database.user.find_unique(
            where={
                "id": user_id
            },
            include={
                'posts': True
            }
        )
        return {"user": user_data}
    except Exception as e:
        raise HTTPException(404, f"user not found {e}")
    finally:
        await database.disconnect()


@app.get("/")
async def get_items():
    await database.connect()
    posts_data = await database.post.find_many(
        include={
            "author": True
        }
    )
    await database.disconnect()
    return {"posts": posts_data}

@app.get("/{id}")
async def get_specific_item(id: int):
    try:
        await database.connect()
        post_data = await database.post.find_unique_or_raise(
            where={
                'id': id
            }
        )
        return {"post": post_data}
    except Exception:
        raise HTTPException(404, "not found")
    finally:
        await database.disconnect()


@app.post('/create')
async def create_item(postDto: PostDto):
    try:
        await database.connect()
        await database.post.create(
            data=postDto.model_dump()
        )
        return {"status": "successful"}
    except Exception as e:
        print(e)
        raise HTTPException(500, "something went wrong")
    finally:
        await database.disconnect()
