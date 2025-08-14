from mcp.server.fastmcp import FastMCP
from database import SessionLocal, Heros, Base, engine

mcp = FastMCP("PopulateDB")
Base.metadata.create_all(bind=engine)


@mcp.tool(
    name="AddHeros",
    description="""
            Adds a new Hero to the database.
            Args:
                input_data(dict): Contains the input data in a dictionary format 
                {
                    hero_name: {"type": "string"},
                    real_name: {"type": "string"},
                    age: {"type": "int"},
                    universe: {"type": "string"},
                }
                example: {
                    hero_name: Spider man,
                    real_name: Peter Parker,
                    age: 18,
                    universe: Marvel,
                }
            Returns:
                str: Confirmation message indicating that hero is added to database.
        """,
)
async def add_heros_to_db(input_data: dict) -> str:
    hero_name = input_data["hero_name"]
    real_name = input_data["real_name"]
    age = input_data["age"]
    universe = input_data["universe"]
    session = SessionLocal()

    try:
        hero = Heros(
            hero_name=hero_name, real_name=real_name, age=age, universe=universe
        )
        session.add(hero)
        session.commit()
        return f"{hero_name} added successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {e}"
    finally:
        session.close()
