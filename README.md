# Onboarding Process for ProtoLaunch

This project provides a guided onboarding process for new users of ProtoLaunch. The onboarding process walks users through key features and workflows, allowing them to skip steps if they are already familiar with the platform.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/onboarding.git
    cd onboarding
    ```

2. Install the package:
    ```sh
    pip install .
    ```

## Usage

1. Create an onboarding instance and add steps:
    ```python
    from onboarding import Onboarding

    onboarding = Onboarding([])
    onboarding.add_step("Welcome", "Welcome to ProtoLaunch!")
    onboarding.add_step("Features", "Learn about key features.")
    onboarding.add_step("Workflows", "Understand the workflows.")
    ```

2. Navigate through the onboarding steps:
    ```python
    step = onboarding.next_step()
    print(step.title, step.description)
    ```

3. Skip a step if already familiar:
    ```python
    step = onboarding.skip_step()
    print(step.title, step.description)
    ```

4. Mark a step as completed:
    ```python
    onboarding.mark_completed()
    ```

5. Save and load the onboarding state:
    ```python
    onboarding.save("onboarding.json")
    loaded_onboarding = Onboarding.load("onboarding.json")
    ```

## Testing

Run the tests using pytest:
