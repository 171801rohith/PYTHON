import edge_tts
import asyncio

async def generate_tts():
    text = "Get ready for a blazing showdown! It's the electric speedster, Pikachu, versus the fiery powerhouse, Charmander! Pikachu takes an early lead with its lightning-fast moves! But Charmander's fire is catching up! It's a photo finish! Looks like it's a tie! What a race!"
    voice = "en-US-GuyNeural"  # Change if needed
    output_file = "test.mp3"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"✅ Speech saved as {output_file}")

asyncio.run(generate_tts())
