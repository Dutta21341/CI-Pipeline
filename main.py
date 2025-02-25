"""Main module for the CI pipeline example."""

def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

def main():
    """Main function to execute the script."""
    print(greet("Sanskar"))

if __name__ == "__main__":
    main()
