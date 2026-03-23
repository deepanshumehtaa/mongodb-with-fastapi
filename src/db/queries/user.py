from ...framework.errors import APIError
from ..models.user import UserDoc
from ..clients.mongo import mgo_db as db


async def create_user(username: str, encrypt_password: str) -> UserDoc:
    existed = await UserDoc.find_one(db, query={"username": username})
    if existed:
        raise APIError("User Already exists!")
    user_doc = UserDoc(username=username, password=encrypt_password)
    return await user_doc.save(db)


async def get_user(username: str, encrypt_password: str) -> UserDoc:
    user = await UserDoc.find_one(
        db,
        query={"username": username, "password": encrypt_password},
    )
    if not user:
        raise APIError(f"User not found / Wrong creds!")
    return user


async def set_user_password(username: str,
                            old_encrypt_password: str,
                            new_encrypt_password: str) -> UserDoc:
    user: UserDoc = await get_user(username, old_encrypt_password)
    user.password = new_encrypt_password
    await user.save(db, fields=("password", ))
    return user


async def get_user_by_id(user_id: int) -> UserDoc:
    user = await UserDoc.get_by_id(db, user_id)
    if not user:
        raise APIError("No User Found")
    return user
