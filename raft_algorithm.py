from manim import *


class RaftVisualization(Scene):
    def construct(self):
        # First scene - Introduction
        self.introduction()
        self.wait(1)

        # Second scene - Cluster nodes
        self.clear()
        self.cluster_nodes()
        self.wait(1)

        # Third scene - Leader election
        self.clear()
        self.leader_election()
        self.wait(1)

        # Fourth scene - Log replication
        self.clear()
        self.log_replication()
        self.wait(1)

        # Final scene - Summary
        self.clear()
        self.summary()
        self.wait(2)

    def introduction(self):
        # Create title
        title = Text("The Raft Consensus Algorithm", font_size=40)
        title.to_edge(UP)

        # Create subtitle
        subtitle = Text("Understandable Distributed Consensus", font_size=30)
        subtitle.next_to(title, DOWN)

        # Create explanation text
        explanation = Text(
            "Raft is a protocol for implementing distributed consensus.", font_size=24
        )
        explanation.next_to(subtitle, DOWN, buff=1)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeIn(explanation))

    def cluster_nodes(self):
        # Create title
        title = Text("Consensus: Getting multiple servers to agree", font_size=36)
        title.to_edge(UP)

        # Create server nodes
        servers = VGroup()
        radius = 0.5
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]

        for i in range(5):
            angle = i * 2 * PI / 5
            position = 2.5 * np.array([np.cos(angle), np.sin(angle), 0])

            server = Circle(radius=radius, color=colors[i])
            server.move_to(position)

            label = Text(f"S{i+1}", font_size=24).move_to(server.get_center())

            node = VGroup(server, label)
            servers.add(node)

        explanation = Text("Let's consider a cluster with 5 servers...", font_size=24)
        explanation.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(explanation))
        self.wait(1)
        self.play(Create(servers))

        new_explanation = Text(
            "Raft achieves consensus through an elected leader.", font_size=24
        )
        new_explanation.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, new_explanation))
        self.wait(1)

    def leader_election(self):
        # Create title
        title = Text("Leader Election", font_size=40)
        title.to_edge(UP)

        # Create server nodes in a row
        servers = VGroup()
        radius = 0.6
        colors = [GRAY, GRAY, GRAY, GRAY, GRAY]  # All start as followers
        labels = ["Follower", "Follower", "Follower", "Follower", "Follower"]

        for i in range(5):
            position = np.array([(i - 2) * 2, 0, 0])

            server = Circle(radius=radius, color=colors[i])
            server.move_to(position)

            top_label = Text(f"S{i+1}", font_size=20).move_to(server.get_center())
            bottom_label = Text(labels[i], font_size=16)
            bottom_label.next_to(server, DOWN, buff=0.2)

            node = VGroup(server, top_label, bottom_label)
            servers.add(node)

        explanation = Text("All nodes start as followers", font_size=24)
        explanation.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Create(servers))
        self.play(FadeIn(explanation))
        self.wait(1)

        # Election timeout
        timeout_text = Text(
            "If followers don't hear from a leader, they become candidates",
            font_size=24,
        )
        timeout_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, timeout_text))
        self.wait(1)

        # Node 3 becomes candidate
        servers[2][0].set_color(YELLOW)
        servers[2][2].become(
            Text("Candidate", font_size=16).next_to(servers[2][0], DOWN, buff=0.2)
        )

        candidate_text = Text(
            "Candidate requests votes from other servers", font_size=24
        )
        candidate_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, candidate_text))
        self.play(
            servers[2][0].animate.set_color(YELLOW),
            Transform(
                servers[2][2],
                Text("Candidate", font_size=16).next_to(servers[2][0], DOWN, buff=0.2),
            ),
        )

        # Add vote arrows
        arrows = VGroup()
        for i in range(5):
            if i != 2:  # Skip candidate
                arrow = Arrow(
                    servers[2][0].get_center(),
                    servers[i][0].get_center(),
                    buff=radius,
                    color=YELLOW,
                )
                arrows.add(arrow)

        self.play(Create(arrows))
        self.wait(1)

        # Nodes vote
        for i in range(5):
            if i != 2:  # Skip candidate
                vote_text = Text("Yes", font_size=14, color=GREEN)
                vote_text.next_to(servers[i][0], UP, buff=0.2)
                self.play(FadeIn(vote_text))
                self.wait(0.3)

        # Node 3 becomes leader
        servers[2][0].set_color(GREEN)
        servers[2][2].become(
            Text("Leader", font_size=16).next_to(servers[2][0], DOWN, buff=0.2)
        )

        leader_text = Text(
            "Once a candidate receives a majority of votes, it becomes leader",
            font_size=24,
        )
        leader_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, leader_text))
        self.play(
            servers[2][0].animate.set_color(GREEN),
            Transform(
                servers[2][2],
                Text("Leader", font_size=16).next_to(servers[2][0], DOWN, buff=0.2),
            ),
        )
        self.wait(1)

    def log_replication(self):
        # Create title
        title = Text("Log Replication", font_size=40)
        title.to_edge(UP)

        # Create server nodes
        servers = VGroup()
        radius = 0.6
        colors = [BLUE, BLUE, GREEN, BLUE, BLUE]  # Middle is leader
        positions = []

        for i in range(5):
            position = np.array([(i - 2) * 2, 0, 0])
            positions.append(position)

            server = Circle(radius=radius, color=colors[i])
            server.move_to(position)

            label = Text(f"S{i+1}", font_size=20).move_to(server.get_center())
            role = "Leader" if i == 2 else "Follower"
            role_label = Text(role, font_size=16).next_to(server, DOWN, buff=0.2)

            # Add log boxes below each server
            log = Rectangle(height=2, width=1, color=WHITE)
            log.next_to(server, DOWN, buff=0.8)

            node = VGroup(server, label, role_label, log)
            servers.add(node)

        explanation = Text("Clients send changes to the leader", font_size=24)
        explanation.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Create(servers))
        self.play(FadeIn(explanation))
        self.wait(1)

        # Client sends request
        client = Circle(radius=0.3, color=RED)
        client.move_to(np.array([0, 3, 0]))
        client_label = Text("Client", font_size=16).next_to(client, UP, buff=0.2)
        client_group = VGroup(client, client_label)

        # Arrow from client to leader
        client_arrow = Arrow(
            client.get_bottom(), servers[2][0].get_top(), buff=0.1, color=RED
        )

        self.play(Create(client_group))
        self.play(Create(client_arrow))

        # Leader adds entry to log
        entry = Rectangle(height=0.4, width=0.8, color=RED, fill_opacity=0.5)
        entry.move_to(servers[2][3].get_top() + DOWN * 0.3)

        log_text = Text("Changes are added to the leader's log", font_size=24)
        log_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, log_text))
        self.play(Create(entry))
        self.wait(1)

        # Leader replicates to followers
        replicate_text = Text(
            "The leader replicates the entry to followers", font_size=24
        )
        replicate_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, replicate_text))

        # Arrows to followers
        follower_arrows = VGroup()
        follower_entries = VGroup()

        for i in range(5):
            if i != 2:  # Skip leader
                arrow = Arrow(
                    servers[2][0].get_center(),
                    servers[i][0].get_center(),
                    buff=radius,
                    color=GREEN,
                )
                follower_arrows.add(arrow)

                # Create entry for this follower
                f_entry = Rectangle(height=0.4, width=0.8, color=RED, fill_opacity=0.5)
                f_entry.move_to(servers[i][3].get_top() + DOWN * 0.3)
                follower_entries.add(f_entry)

        self.play(Create(follower_arrows))
        self.play(Create(follower_entries))

        # Once majority confirms, leader commits
        commit_text = Text(
            "Once a majority of followers confirm, the entry is committed", font_size=24
        )
        commit_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, commit_text))

        # Show commitment
        committed_entry = entry.copy()
        committed_entry.set_color(GREEN)

        self.play(Transform(entry, committed_entry))
        self.wait(1)

        # Followers also commit
        for e in follower_entries:
            committed_e = e.copy()
            committed_e.set_color(GREEN)
            self.play(Transform(e, committed_e), run_time=0.3)

        # Leader notifies client
        response_arrow = Arrow(
            servers[2][0].get_top(), client.get_bottom(), buff=0.1, color=GREEN
        )

        response_text = Text("The leader notifies the client of success", font_size=24)
        response_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(explanation, response_text))
        self.play(Create(response_arrow))
        self.wait(1)

    def summary(self):
        # Create title
        title = Text("Raft Consensus Algorithm", font_size=40)
        title.to_edge(UP)

        # Create summary points
        summary = VGroup()

        points = [
            "1. Leader Election: Nodes elect a single leader",
            "2. Log Replication: Leader manages the replication of logs",
            "3. Safety: Ensures all nodes see the same sequence of state changes",
            "4. Membership Changes: Allows for configuration changes",
            "5. Understandability: Designed to be easier to understand than other algorithms",
        ]

        for i, point in enumerate(points):
            text = Text(point, font_size=24)
            text.to_edge(LEFT, buff=1)
            text.shift(DOWN * (i * 0.8))
            summary.add(text)

        reference = Text("Learn more at: raft.github.io", font_size=20)
        reference.to_edge(DOWN)

        self.play(Write(title))

        for point in summary:
            self.play(FadeIn(point))
            self.wait(0.5)

        self.play(FadeIn(reference))


if __name__ == "__main__":
    # Uncomment to render the animation (quality can be "low", "medium", "high", "ultra_high")
    # Command to render: python -m manim -pql raft_algorithm.py RaftVisualization
    pass
