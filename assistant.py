from livekit.agents import llm
from typing import Annotated

class AssistantFunction(llm.FunctionContext):
    """This class is used to define functions that will be called by the assistant."""

    @llm.ai_callable(
        description=(
            "Called when asked to evaluate something that would require vision capabilities"
        )
    )

    async def image(
        self,
        user_msg: Annotated[
            str,
            llm.TypeInfo(
                description="The user message that triggered this function"
            ),
        ],
    ):
        print(f"[LOG] Message triggering vision capabilities: {user_msg}")

        return None
    
    @llm.ai_callable(
        description=(
            "Called when asked to tell anything something about a person or the user himself accurately and in good detail"
        )
    )

    async def person_in_frame(
        self,
        user_msg: Annotated[
            str,
            llm.TypeInfo(
                description="The user message is requesting details about a person in the frame"
            ),
        ],
    ):
        print(f"[LOG] Person detection requested: {user_msg}")

        return None
