import asyncio
import random
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Vertical, VerticalScroll, Container, Horizontal
from textual.widgets import Input, Static, RichLog, Label
from textual.binding import Binding

# Custom ASCII Header
AGENT_ART = r"""
███╗   ███╗███████╗██████╗ ██╗██████╗ ██╗ █████╗ ███╗   ██╗
████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██║██╔══██╗████╗  ██║
██╔████╔██║█████╗  ██████╔╝██║██║  ██║██║███████║██╔██╗ ██║
██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║  ██║██║██╔══██║██║╚██╗██║
██║ ╚═╝ ██║███████╗██║  ██║██║██████╔╝██║██║  ██║██║ ╚████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                           
"""

AGENT_DESCRIPTION = "High-performance Agentic Interface v1.0.4\nTechnical Orchestrator for Real-time Systems"

class ToolCall(Static):
    """A widget to represent a nested tool call."""
    def __init__(self, tool_name: str, args: str, **kwargs):
        super().__init__(**kwargs)
        self.tool_name = tool_name
        self.args = args
        self.start_time = datetime.now()

    def compose(self) -> ComposeResult:
        yield Static(f"  [cyan]󰆍 {self.tool_name}[/cyan] ([dim]\"{self.args}\"[/dim])", classes="tool-main")
        yield Static("  [dim]└[/dim] [yellow]pending...[/yellow]", id="timer", classes="tool-sub")

    def finish(self):
        elapsed = int((datetime.now() - self.start_time).total_seconds() * 1000)
        timer_label = self.query_one("#timer", Static)
        timer_label.update(f"  [dim]└[/dim] [dim]in {elapsed}ms[/dim]")
        timer_label.remove_class("pending")
        timer_label.add_class("finished")

class MeridianApp(App):
    """A sophisticated, high-performance CLI Agent interface."""

    CSS = """
    Screen {
        background: #0d0d0d;
    }

    #app-container {
        height: 100%;
        width: 100%;
        padding: 0 4;
    }

    #header-container {
        height: auto;
        margin-top: 1;
        margin-bottom: 1;
        text-align: center;
    }

    #header-art {
        color: #333333;
    }

    #header-description {
        color: #555555;
        text-style: italic;
    }

    #response-area {
        height: 1fr;
        border: solid #1a1a1a;
        padding: 1 2;
        background: #0d0d0d;
        color: #d1d1d1;
    }

    .user-msg {
        color: #7799aa;
        margin-top: 1;
        text-style: bold;
    }

    .agent-label {
        color: #32CD32;
        text-style: bold;
        margin-top: 1;
    }

    .agent-response {
        color: #d1d1d1;
        margin-bottom: 1;
    }

    .summary-box {
        background: #151515;
        border-left: solid #32CD32;
        padding: 0 1;
        margin: 1 0;
    }

    .tool-main {
        margin-top: 0;
    }
    
    .tool-sub {
        color: #555555;
        margin-bottom: 1;
    }

    #log-divider {
        color: #222222;
        text-align: center;
        width: 100%;
        margin-top: 1;
    }

    #log-container {
        height: 8;
        background: #0a0a0a;
        margin-bottom: 1;
    }

    #agent-logs {
        height: 1fr;
        color: #708090;
        padding: 0 1;
    }

    #input-area {
        height: auto;
        border: solid #333333;
        background: #111111;
        padding: 0 1;
        margin-bottom: 1;
    }

    #prompt {
        color: #555555;
        padding: 1 0 0 0;
    }

    #input-box {
        border: none;
        background: transparent;
        color: #eeeeee;
        width: 1fr;
    }

    #input-box:focus {
        border: none;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=True),
        Binding("ctrl+l", "clear_logs", "Clear Logs", show=True),
    ]

    def compose(self) -> ComposeResult:
        with Container(id="app-container"):
            with Vertical(id="header-container"):
                yield Static(AGENT_ART, id="header-art")
                yield Static(AGENT_DESCRIPTION, id="header-description")
            
            with VerticalScroll(id="response-area"):
                yield Static("[dim]Session started. Kernel v1.0.4-stable-prod[/dim]", classes="system-msg")
            
            yield Static("--- Agent Logs ---", id="log-divider")
            with Vertical(id="log-container"):
                yield RichLog(id="agent-logs", highlight=True, markup=True)
            
            with Horizontal(id="input-area"):
                yield Label(">", id="prompt")
                yield Input(placeholder="Ask anything...", id="input-box")

    def on_mount(self) -> None:
        self.query_one("#input-box").focus()
        self.log_technical("System", "Handshake complete. Memory initialized.")

    def log_technical(self, component: str, message: str) -> None:
        """Log with technical formatting."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_widget = self.query_one("#agent-logs", RichLog)
        log_widget.write(f"[dim]{timestamp}[/dim] [[bold slate_gray]{component}[/bold slate_gray]] {message}")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        user_text = event.value.strip()
        if not user_text:
            return

        input_widget = self.query_one("#input-box", Input)
        input_widget.value = ""

        response_area = self.query_one("#response-area", VerticalScroll)
        
        # 1. User Input
        response_area.mount(Static(f"User: {user_text}", classes="user-msg"))
        
        # 2. Extract Intent
        self.log_technical("Intent Extractor", "Successfully extracted scope and parameters...")
        await asyncio.sleep(0.4)

        # 3. Simulate Tool Call
        tool = ToolCall(tool_name="fetchNews", args=user_text[:15] + "...")
        response_area.mount(tool)
        response_area.scroll_end(animate=True)
        
        self.log_technical("Agent loop", "Executing 1 tool call(s) concurrently...")
        
        # Simulate processing time
        await asyncio.sleep(random.uniform(0.8, 1.5))
        tool.finish()
        
        self.log_technical("Orchestrator", "Tool execution complete. Synthesizing final response.")

        # 4. Final Agent Response
        response_area.mount(Static("Agent", classes="agent-label"))
        
        summary_content = (
            "[bold white]* Summary of Information:[/bold white]\n"
            "  * Identified 3 key data points relevant to query.\n"
            "  * Cross-referenced technical documentation and logs.\n"
            "  * Verified state consistency across layers."
        )
        response_area.mount(Static(summary_content, classes="summary-box"))
        
        answer_text = f"I've analyzed the request for '{user_text}'. The system state is currently stable and all operational metrics are within expected parameters."
        response_area.mount(Static(answer_text, classes="agent-response"))
        
        response_area.scroll_end(animate=True)
        self.log_technical("System", "Response delivered. Awaiting next cycle.")

    def action_clear_logs(self) -> None:
        self.query_one("#agent-logs", RichLog).clear()
        self.log_technical("System", "Log buffer cleared.")

if __name__ == "__main__":
    app = MeridianApp()
    app.run()
