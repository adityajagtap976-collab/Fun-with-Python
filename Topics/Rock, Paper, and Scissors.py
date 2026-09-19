import random
import tkinter as tk
from enum import Enum
from tkinter import messagebox, ttk
from typing import Literal


class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class ScoreBoard:
    """Manages match scores and target score limits."""

    def __init__(self, target_score: int = 3):
        self.target_score = target_score
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

    def record_win(self) -> None:
        self.player_score += 1

    def record_loss(self) -> None:
        self.computer_score += 1

    def record_tie(self) -> None:
        self.ties += 1

    def is_game_over(self) -> bool:
        return (
            self.player_score >= self.target_score
            or self.computer_score >= self.target_score
        )

    def reset(self, target_score: int) -> None:
        self.target_score = target_score
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0


class RPSGuiApp:
    """Tkinter Graphical User Interface for Rock Paper Scissors."""

    # Emojis for clean visual representation
    CHOICE_EMOJIS = {  # noqa: RUF012
        Choice.ROCK: "🪨 Rock",
        Choice.PAPER: "📄 Paper",
        Choice.SCISSORS: "✂️ Scissors",
    }

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("450x520")
        self.root.resizable(False, False)

        self.scoreboard = ScoreBoard(target_score=3)

        self._build_ui()

    def _build_ui(self) -> None:
        # --- Top Title & Target Score Selection ---
        title_label = tk.Label(
            self.root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold")
        )
        title_label.pack(pady=(15, 5))

        target_frame = tk.Frame(self.root)
        target_frame.pack(pady=5)

        tk.Label(
            target_frame, text="Target Score (First to):", font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        self.target_spinbox = ttk.Spinbox(
            target_frame, from_=1, to=10, width=5, font=("Helvetica", 10)
        )
        self.target_spinbox.set(3)
        self.target_spinbox.pack(side=tk.LEFT)

        self.reset_btn = ttk.Button(
            target_frame, text="New Match", command=self._start_new_match
        )
        self.reset_btn.pack(side=tk.LEFT, padx=10)

        # --- Scoreboard Display Frame ---
        score_frame = tk.LabelFrame(
            self.root,
            text=" Scoreboard ",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=10,
        )
        score_frame.pack(fill="x", padx=20, pady=10)

        self.player_score_lbl = tk.Label(
            score_frame, text="You: 0", font=("Helvetica", 12, "bold"), fg="#1b5e20"
        )
        self.player_score_lbl.grid(row=0, column=0, padx=20)

        self.ties_lbl = tk.Label(
            score_frame, text="Ties: 0", font=("Helvetica", 12), fg="#616161"
        )
        self.ties_lbl.grid(row=0, column=1, padx=20)

        self.computer_score_lbl = tk.Label(
            score_frame,
            text="Computer: 0",
            font=("Helvetica", 12, "bold"),
            fg="#b71c1c",
        )
        self.computer_score_lbl.grid(row=0, column=2, padx=20)

        # --- Arena Match Results Display ---
        arena_frame = tk.Frame(self.root, relief=tk.GROOVE, bd=2, bg="#f5f5f5")
        arena_frame.pack(fill="x", padx=20, pady=10, ipady=10)

        self.p_move_lbl = tk.Label(
            arena_frame, text="Your Move: —", font=("Helvetica", 11), bg="#f5f5f5"
        )
        self.p_move_lbl.pack(anchor="w", padx=15, pady=2)

        self.c_move_lbl = tk.Label(
            arena_frame, text="Computer Move: —", font=("Helvetica", 11), bg="#f5f5f5"
        )
        self.c_move_lbl.pack(anchor="w", padx=15, pady=2)

        self.result_lbl = tk.Label(
            arena_frame,
            text="Select a move to begin!",
            font=("Helvetica", 12, "bold"),
            bg="#f5f5f5",
            fg="#0d47a1",
        )
        self.result_lbl.pack(pady=(10, 0))

        # --- Player Action Buttons ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.rock_btn = tk.Button(
            btn_frame,
            text="🪨 Rock",
            font=("Helvetica", 11, "bold"),
            width=10,
            height=2,
            bg="#e0e0e0",
            command=lambda: self._play_round(Choice.ROCK),
        )
        self.rock_btn.grid(row=0, column=0, padx=5)

        self.paper_btn = tk.Button(
            btn_frame,
            text="📄 Paper",
            font=("Helvetica", 11, "bold"),
            width=10,
            height=2,
            bg="#e0e0e0",
            command=lambda: self._play_round(Choice.PAPER),
        )
        self.paper_btn.grid(row=0, column=1, padx=5)

        self.scissors_btn = tk.Button(
            btn_frame,
            text="✂️ Scissors",
            font=("Helvetica", 11, "bold"),
            width=10,
            height=2,
            bg="#e0e0e0",
            command=lambda: self._play_round(Choice.SCISSORS),
        )
        self.scissors_btn.grid(row=0, column=2, padx=5)

    def _play_round(self, player_choice: Choice) -> None:
        """Executes round evaluation using zero-indexed modulo arithmetic."""
        computer_choice = random.choice(list(Choice))

        # Core Modulo Arithmetic Evaluation
        result = (player_choice.value - computer_choice.value) % 3

        # Update visual labels for moves
        self.p_move_lbl.config(text=f"Your Move: {self.CHOICE_EMOJIS[player_choice]}")
        self.c_move_lbl.config(
            text=f"Computer Move: {self.CHOICE_EMOJIS[computer_choice]}"
        )

        # Evaluate outcome
        if result == 0:
            self.result_lbl.config(text="It's a tie!", fg="#616161")
            self.scoreboard.record_tie()
        elif result == 1:
            self.result_lbl.config(text="You win this round! 🎉", fg="#2e7d32")
            self.scoreboard.record_win()
        else:
            self.result_lbl.config(text="Computer wins this round! 🤖", fg="#c62828")
            self.scoreboard.record_loss()

        self._update_scoreboard_ui()
        self._check_match_winner()

    def _update_scoreboard_ui(self) -> None:
        """Refreshes the scoreboard counters in the UI."""
        target = self.scoreboard.target_score
        self.player_score_lbl.config(
            text=f"You: {self.scoreboard.player_score}/{target}"
        )
        self.computer_score_lbl.config(
            text=f"Computer: {self.scoreboard.computer_score}/{target}"
        )
        self.ties_lbl.config(text=f"Ties: {self.scoreboard.ties}")

    def _check_match_winner(self) -> None:
        """Checks if target score has been reached and shows popup notification."""
        if self.scoreboard.is_game_over():
            self._set_buttons_state(enabled=False)

            if self.scoreboard.player_score >= self.scoreboard.target_score:
                messagebox.showinfo(
                    "Match Finished", "🏆 Congratulations! You won the match!"
                )
            else:
                messagebox.showinfo(
                    "Match Finished", "💻 Game Over! Computer won the match."
                )

    def _start_new_match(self) -> None:
        """Resets scores, UI elements, and button states for a new game."""
        try:
            new_target = int(self.target_spinbox.get())
            if new_target <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please set a target score greater than 0."
            )
            return

        self.scoreboard.reset(new_target)
        self._update_scoreboard_ui()

        self.p_move_lbl.config(text="Your Move: —")
        self.c_move_lbl.config(text="Computer Move: —")
        self.result_lbl.config(text="Select a move to begin!", fg="#0d47a1")
        self._set_buttons_state(enabled=True)

    def _set_buttons_state(self, enabled: bool) -> None:
        """Utility to disable choice buttons when match completes."""
        state: Literal["normal", "disabled"] = "normal" if enabled else "disabled"
        self.rock_btn.config(state=state)
        self.paper_btn.config(state=state)
        self.scissors_btn.config(state=state)


if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGuiApp(root)
    root.mainloop()
