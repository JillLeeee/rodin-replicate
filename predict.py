class Predictor:
    def setup(self):
        print("Rodin Model setup complete.")

    def predict(self, prompt: str = "A futuristic chair") -> str:
        print(f"Generating model for: {prompt}")
        # This is a placeholder — real output should be a 3D model
        return f"https://yourhost.com/generated_models/{prompt.replace(' ', '_')}.glb"
