from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.product.models import Product
from src.product.schemas import Product as ProductSchema
from typing import List
from pydantic import parse_obj_as

router = APIRouter(prefix="/product", tags=["product"])


@router.get("/all_products", response_model=List[ProductSchema])
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/create_product")
async def add_product(product_name: str, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(name=product_name)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
