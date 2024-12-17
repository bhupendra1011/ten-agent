from ten import (
    AudioFrame,
    VideoFrame,
    AsyncExtension,
    AsyncTenEnv,
    Cmd,
    StatusCode,
    CmdResult,
    Data,
)
from ten_ai_base.const import DATA_OUT_NAME, DATA_OUT_PROPERTY_END_OF_SEGMENT, DATA_OUT_PROPERTY_TEXT

# on_data() method receives the input text (text_input) from LLM or another extension.

class HelloWorldExtension(AsyncExtension):
    async def on_init(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_info("on_init hello_world")

    async def on_start(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_info("on_start hello_world")

        # Initialize resources or configurations if needed
        # For example, reading properties or setting up initial states
        pass

    async def on_stop(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_info("on_stop hello_world")

        # Clean up resources if needed
        pass

    async def on_deinit(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_info("on_deinit hello_world")
        ten_env.on_deinit_done()

    async def on_cmd(self, ten_env: AsyncTenEnv, cmd: Cmd) -> None:
        cmd_name = cmd.get_name()
        ten_env.log_info(f"on_cmd name  hello_world {cmd_name}")

        # Process commands if needed (but not used here)
        cmd_result = CmdResult.create(StatusCode.OK)
        ten_env.return_result(cmd_result, cmd)

    async def on_data(self, ten_env: AsyncTenEnv, data: Data) -> None:
        data_name = data.get_name()
  
        ten_env.log_info(f"hello_world => property name: {data_name}  text : {data.get_property_string('text')}")

        if data_name == DATA_OUT_NAME:
            # Extract the text input from the data
            user_input = data.get_property_string(DATA_OUT_PROPERTY_TEXT)
            # Generate the response based on the input
            response_text = self.generate_response(user_input,ten_env)
            # Create a new data object to send the response
            response_data = Data.create(DATA_OUT_NAME)
            response_data.set_property_string(DATA_OUT_PROPERTY_TEXT, response_text)
            response_data.set_property_bool(
                DATA_OUT_PROPERTY_END_OF_SEGMENT, True
            )
            
            # Send the response back to llm or other extensions
            ten_env.send_data(response_data)
            
            ten_env.log_info(f"Sent response from hello_world: {response_text}")

    def generate_response(self,user_input: str,ten_env:AsyncTenEnv) -> str:
        # Generate a response based on the input text
        ten_env.log_info(f"compare function hello_world {user_input}")
        if "how are you" in user_input.lower():
            return "Hello, World!"
        else:
            return "I'm here to assist you."

    async def on_audio_frame(
        self, ten_env: AsyncTenEnv, audio_frame: AudioFrame
    ) -> None:
        audio_frame_name = audio_frame.get_name()
        ten_env.log_info(f"on_audio_frame hello_world name {audio_frame_name}")

        # Process audio frames if needed (not needed for hello_world)
        pass

    async def on_video_frame(
        self, ten_env: AsyncTenEnv, video_frame: VideoFrame
    ) -> None:
        video_frame_name = video_frame.get_name()
        ten_env.log_info(f"on_video_frame hello_world name {video_frame_name}")

        # Process video frames if needed (not needed for hello_world)
        pass
