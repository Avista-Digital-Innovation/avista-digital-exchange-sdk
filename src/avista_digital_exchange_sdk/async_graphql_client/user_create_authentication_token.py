# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AuthenticationTokenType


class UserCreateAuthenticationToken(BaseModel):
    user_create_authentication_token: Optional[
        "UserCreateAuthenticationTokenUserCreateAuthenticationToken"
    ] = Field(alias="user_createAuthenticationToken")


class UserCreateAuthenticationTokenUserCreateAuthenticationToken(BaseModel):
    date_created: str = Field(alias="dateCreated")
    date_expires: str = Field(alias="dateExpires")
    last_active: Optional[str] = Field(alias="lastActive")
    name: str
    scope: Optional[List[Optional[str]]]
    token_id: str = Field(alias="tokenId")
    token_type: Optional[AuthenticationTokenType] = Field(alias="tokenType")
    token_value: Optional[str] = Field(alias="tokenValue")
    user_id: str = Field(alias="userId")


UserCreateAuthenticationToken.update_forward_refs()
UserCreateAuthenticationTokenUserCreateAuthenticationToken.update_forward_refs()
