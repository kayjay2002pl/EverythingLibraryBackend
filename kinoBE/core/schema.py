from pydantic import ConfigDict, BaseModel


class SchemaConfig(BaseModel):
    """
    Basic pydantic model settings
    """
    model_config = ConfigDict(coerce_numbers_to_str=True)

