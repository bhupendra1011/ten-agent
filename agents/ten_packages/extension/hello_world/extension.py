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

# on_data() method receives the input text (text_input) from LLM or another extension.

class HelloWorldExtension(AsyncExtension):
    async def on_init(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_debug("on_init")

    async def on_start(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_debug("on_start")

        # Initialize resources or configurations if needed
        # For example, reading properties or setting up initial states
        pass

    async def on_stop(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_debug("on_stop")

        # Clean up resources if needed
        pass

    async def on_deinit(self, ten_env: AsyncTenEnv) -> None:
        ten_env.log_debug("on_deinit")
        ten_env.on_deinit_done()

    async def on_cmd(self, ten_env: AsyncTenEnv, cmd: Cmd) -> None:
        cmd_name = cmd.get_name()
        ten_env.log_debug(f"on_cmd name {cmd_name}")

        # Process commands if needed (but not used here)
        cmd_result = CmdResult.create(StatusCode.OK)
        ten_env.return_result(cmd_result, cmd)

    async def on_data(self, ten_env: AsyncTenEnv, data: Data) -> None:
        data_name = data.get_name()
        ten_env.log_debug(f"Received data: {data_name}")

        if data_name == "text_input":
            # Extract the text input from the data
            user_input = data.get_property("text")
            # Generate the response based on the input
            response_text = self.generate_response(user_input)
            # Create a new data object to send the response
            response_data = Data.create("text_output")
            response_data.set_property("text", response_text)
            # Send the response back to llm or other extensions
            ten_env.send_data("chatgpt", "llm", response_data)
            ten_env.log_debug(f"Sent response: {response_text}")

    def generate_response(self, user_input: str) -> str:
        # Generate a response based on the input text
        if "how are you" in user_input.lower():
            return "Hello, World!"
        else:
            return "I'm here to assist you."

    async def on_audio_frame(
        self, ten_env: AsyncTenEnv, audio_frame: AudioFrame
    ) -> None:
        audio_frame_name = audio_frame.get_name()
        ten_env.log_debug(f"on_audio_frame name {audio_frame_name}")

        # Process audio frames if needed (not needed for hello_world)
        pass

    async def on_video_frame(
        self, ten_env: AsyncTenEnv, video_frame: VideoFrame
    ) -> None:
        video_frame_name = video_frame.get_name()
        ten_env.log_debug(f"on_video_frame name {video_frame_name}")

        # Process video frames if needed (not needed for hello_world)
        pass
