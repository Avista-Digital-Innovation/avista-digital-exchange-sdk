# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AuthenticationTokenType


class UserListAuthenticationTokens(BaseModel):
    user_list_authentication_tokens: Optional[
        List[Optional["UserListAuthenticationTokensUserListAuthenticationTokens"]]
    ] = Field(alias="user_listAuthenticationTokens")


class UserListAuthenticationTokensUserListAuthenticationTokens(BaseModel):
    date_created: str = Field(alias="dateCreated")
    date_expires: str = Field(alias="dateExpires")
    last_active: Optional[str] = Field(alias="lastActive")
    name: str
    scope: Optional[List[Optional[str]]]
    token_id: str = Field(alias="tokenId")
    token_type: Optional[AuthenticationTokenType] = Field(alias="tokenType")
    token_value: Optional[str] = Field(alias="tokenValue")
    user_id: str = Field(alias="userId")


UserListAuthenticationTokens.update_forward_refs()
UserListAuthenticationTokensUserListAuthenticationTokens.update_forward_refs()
