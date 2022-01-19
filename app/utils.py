from passlib.context import CryptContext
# hashing password - using bcrypt for scheme of hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)

# verifying when users login with their password, it hashes it and compares to the hashed password in database


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
