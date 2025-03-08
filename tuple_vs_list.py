import os
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService

from _utils import create_code_scene


class TupleVsList(VoiceoverScene):
    def construct(self):
        # Use ElevenLabs if API key is available, otherwise fallback to GTTS
        if os.environ.get("ELEVENLABS_API_KEY"):
            self.set_speech_service(ElevenLabsService(voice_id="UgBBYS2sOqTuMpoF3BR0"))
        else:
            raise Exception("ElevenLabs API key not found. Please set it or create a .env file with the variable.")

        # Introduction
        title = Text("Python: Tuples vs Lists").scale(0.8)
        
        with self.voiceover(
            """
            Hello! In today's video, I'll explain the difference between tuples and lists in Python.
            <bookmark mark='title'/>
            
            We'll cover their syntax, mutability, performance, and common use cases with code examples.
            <bookmark mark='intro_end'/>
            """
        ) as tracker:
            self.wait_until_bookmark("title")
            self.play(Write(title), run_time=tracker.time_until_bookmark("intro_end"))
        
        self.play(FadeOut(title))
        
        # Disclaimer
        with self.voiceover(
            """
            Before we begin, a quick disclaimer:
            The voiceover for this video is generated using Eleven Labs, and the source code
            for this video is available in the description.
            """
        ):
            disclaimer = Text("Disclaimer", color=YELLOW).scale(0.7)
            disclaimer_text = Text(
                "Voice: Eleven Labs\nSource code in description",
                color=GRAY
            ).scale(0.5)
            disclaimer_text.next_to(disclaimer, DOWN)
            
            disclaimer_group = VGroup(disclaimer, disclaimer_text)
            self.play(FadeIn(disclaimer_group))
            self.wait(1)
            self.play(FadeOut(disclaimer_group))
        
        # Syntax Comparison
        with self.voiceover(
            """
            Let's start with the basic syntax. 
            <bookmark mark='syntax'/>
            
            Lists are created using square brackets. 
            <bookmark mark='list_syntax'/>
            
            While tuples use parentheses. 
            <bookmark mark='tuple_syntax'/>
            
            You can also create a tuple without parentheses by just separating values with commas,
            but it's a good practice to use parentheses for clarity. 
            <bookmark mark='syntax_end'/>
            """
        ) as tracker:
            self.wait_until_bookmark("syntax")
            
            syntax_title = Text("Syntax", color=BLUE).scale(0.8).to_edge(UP)
            self.play(Write(syntax_title))
            
            list_code = create_code_scene("my_list = [1, 2, 3, 'apple', True]").scale(0.8)
            list_code.next_to(syntax_title, DOWN, buff=0.5)
            
            tuple_code = create_code_scene("my_tuple = (1, 2, 3, 'apple', True)").scale(0.8)
            tuple_code.next_to(list_code, DOWN, buff=0.5)
            
            tuple_no_parens = create_code_scene("another_tuple = 1, 2, 3, 'apple', True").scale(0.8)
            tuple_no_parens.next_to(tuple_code, DOWN, buff=0.5)
            
            self.wait_until_bookmark("list_syntax")
            self.play(Create(list_code))
            
            self.wait_until_bookmark("tuple_syntax")
            self.play(Create(tuple_code))
            
            self.wait_until_bookmark("syntax_end")
            self.play(Create(tuple_no_parens))
        
        self.wait(1)
        self.play(FadeOut(list_code), FadeOut(tuple_code), FadeOut(tuple_no_parens))
        
        # Mutability
        with self.voiceover(
            """
            The key difference between tuples and lists is mutability. 
            <bookmark mark='mutability'/>
            
            Lists are mutable, which means you can change, add, or remove elements after creation. 
            <bookmark mark='list_mutability'/>
            
            Let's see some examples of list operations. 
            <bookmark mark='list_ops'/>
            """
        ) as tracker:
            self.wait_until_bookmark("mutability")
            
            self.play(Transform(syntax_title, Text("Mutability", color=BLUE).scale(0.8).to_edge(UP)))
            
            mutability_text = Text("Lists: Mutable\nTuples: Immutable", color=WHITE).scale(0.7)
            mutability_text.next_to(syntax_title, DOWN, buff=0.5)
            
            self.wait_until_bookmark("list_mutability")
            self.play(Write(mutability_text))
            
            self.wait_until_bookmark("list_ops")
            self.play(FadeOut(mutability_text))
        
        # List operations
        with self.voiceover(
            """
            With lists, you can modify elements. 
            <bookmark mark='list_modify'/>
            
            Add new elements. 
            <bookmark mark='list_add'/>
            
            Or remove elements. 
            <bookmark mark='list_remove'/>
            """
        ) as tracker:
            list_init = create_code_scene("fruits = ['apple', 'banana', 'cherry']").scale(0.7)
            list_init.next_to(syntax_title, DOWN, buff=0.5)
            self.play(Create(list_init))
            
            self.wait_until_bookmark("list_modify")
            list_modify = create_code_scene("fruits[0] = 'orange'  # Now: ['orange', 'banana', 'cherry']").scale(0.7)
            list_modify.next_to(list_init, DOWN, buff=0.5)
            self.play(Create(list_modify))
            
            self.wait_until_bookmark("list_add")
            list_add = create_code_scene("fruits.append('mango')  # Now: ['orange', 'banana', 'cherry', 'mango']").scale(0.7)
            list_add.next_to(list_modify, DOWN, buff=0.5)
            self.play(Create(list_add))
            
            self.wait_until_bookmark("list_remove")
            list_remove = create_code_scene("fruits.remove('banana')  # Now: ['orange', 'cherry', 'mango']").scale(0.7)
            list_remove.next_to(list_add, DOWN, buff=0.5)
            self.play(Create(list_remove))
        
        self.wait(1)
        list_ops_group = VGroup(list_init, list_modify, list_add, list_remove)
        
        # Tuple immutability
        with self.voiceover(
            """
            Tuples, on the other hand, are immutable. 
            <bookmark mark='tuple_immutable'/>
            
            Once created, you cannot change their elements. 
            <bookmark mark='tuple_error'/>
            
            If you try to modify a tuple, Python will raise a TypeError. 
            <bookmark mark='tuple_end'/>
            """
        ) as tracker:
            self.wait_until_bookmark("tuple_immutable")
            
            self.play(FadeOut(list_ops_group))
            
            tuple_init = create_code_scene("fruits = ('apple', 'banana', 'cherry')").scale(0.7)
            tuple_init.next_to(syntax_title, DOWN, buff=0.5)
            self.play(Create(tuple_init))
            
            self.wait_until_bookmark("tuple_error")
            tuple_error = create_code_scene("""# This will raise a TypeError
fruits[0] = 'orange'  

# TypeError: 'tuple' object does not support item assignment""").scale(0.7)
            tuple_error.next_to(tuple_init, DOWN, buff=0.5)
            self.play(Create(tuple_error))
            
            self.wait_until_bookmark("tuple_end")
            error_highlight = SurroundingRectangle(tuple_error, color=RED)
            self.play(Create(error_highlight))
        
        self.wait(1)
        self.play(FadeOut(tuple_init), FadeOut(tuple_error), FadeOut(error_highlight))
        
        # Performance
        with self.voiceover(
            """
            Let's talk about performance. 
            <bookmark mark='performance'/>
            
            Tuples are generally more efficient than lists in terms of memory usage and performance. 
            <bookmark mark='perf_explain'/>
            
            Since tuples are immutable, Python can optimize their use internally. 
            <bookmark mark='perf_end'/>
            """
        ) as tracker:
            self.wait_until_bookmark("performance")
            
            self.play(Transform(syntax_title, Text("Performance", color=BLUE).scale(0.8).to_edge(UP)))
            
            performance_text = Text(
                "Tuples:\n• Lower memory usage\n• Faster creation\n• Can be used as dictionary keys",
                color=WHITE
            ).scale(0.55)
            performance_text.next_to(syntax_title, DOWN, buff=0.5)
            
            self.wait_until_bookmark("perf_explain")
            self.play(Write(performance_text))
            
            self.wait_until_bookmark("perf_end")
            perf_highlight = SurroundingRectangle(performance_text, color=GREEN)
            self.play(Create(perf_highlight))
        
        self.wait(1)
        self.play(FadeOut(performance_text), FadeOut(perf_highlight))
        
        # Use cases
        with self.voiceover(
            """
            When should you use lists versus tuples? 
            <bookmark mark='use_cases'/>
            
            Use lists when you need a collection that might change, 
            <bookmark mark='list_cases'/>
            such as a shopping cart, a list of active users, or any data that needs to be modified.
            
            Use tuples for collections that should not change, 
            <bookmark mark='tuple_cases'/>
            like coordinates, RGB values, or database records.
            
            Tuples can also be used as dictionary keys, while lists cannot. 
            <bookmark mark='dict_keys'/>
            """
        ) as tracker:
            self.wait_until_bookmark("use_cases")
            
            self.play(Transform(syntax_title, Text("Use Cases", color=BLUE).scale(0.8).to_edge(UP)))
            
            self.wait_until_bookmark("list_cases")
            list_cases = Text(
                "Lists: When data needs to change",
                color=WHITE
            ).scale(0.55)
            list_cases.next_to(syntax_title, DOWN, buff=0.5)
            self.play(Write(list_cases))
            
            list_examples = create_code_scene("""# Examples for lists
shopping_cart = ['bread', 'milk', 'eggs']
active_users = ['user1', 'user2', 'user3']
measurements = [98.6, 99.2, 97.9]  # May need updates""").scale(0.65)
            list_examples.next_to(list_cases, DOWN, buff=0.3)
            self.play(Create(list_examples))
            
            self.wait_until_bookmark("tuple_cases")
            tuple_cases = Text(
                "Tuples: When data should remain constant",
                color=WHITE
            ).scale(0.55)
            tuple_cases.next_to(list_examples, DOWN, buff=0.4)
            self.play(Write(tuple_cases))
            
            tuple_examples = create_code_scene("""# Examples for tuples
point = (4, 5)  # x,y coordinate
rgb = (255, 0, 0)  # Red color
person = ('John', 'Doe', 35)  # Name and age""").scale(0.65)
            tuple_examples.next_to(tuple_cases, DOWN, buff=0.3)
            self.play(Create(tuple_examples))
            
            self.wait_until_bookmark("dict_keys")
            dict_example = create_code_scene("""# Tuples as dictionary keys (valid)
locations = {(40.7128, -74.0060): 'New York City'}

# Lists as dictionary keys (invalid)
# locations = {[40.7128, -74.0060]: 'New York City'}  # TypeError""").scale(0.6)
            dict_example.next_to(tuple_examples, DOWN, buff=0.4)
            self.play(Create(dict_example))
        
        self.wait(1)
        
        # Packing and unpacking
        with self.voiceover(
            """
            Both tuples and lists support packing and unpacking, 
            <bookmark mark='packing'/>
            
            but this is more commonly used with tuples. 
            <bookmark mark='packing_example'/>
            
            Tuple unpacking is especially useful for returning multiple values from a function. 
            <bookmark mark='function_return'/>
            """
        ) as tracker:
            self.wait_until_bookmark("packing")
            
            self.play(
                FadeOut(list_cases),
                FadeOut(list_examples),
                FadeOut(tuple_cases),
                FadeOut(tuple_examples),
                FadeOut(dict_example)
            )
            
            self.play(Transform(syntax_title, Text("Packing & Unpacking", color=BLUE).scale(0.8).to_edge(UP)))
            
            self.wait_until_bookmark("packing_example")
            packing_example = create_code_scene("""# Tuple packing and unpacking
coordinates = 10, 20  # Packing values into a tuple
x, y = coordinates    # Unpacking tuple into variables

# List unpacking works too
a, b, c = [1, 2, 3]   # Unpacking list into variables""").scale(0.7)
            packing_example.next_to(syntax_title, DOWN, buff=0.5)
            self.play(Create(packing_example))
            
            self.wait_until_bookmark("function_return")
            function_example = create_code_scene("""# Returning multiple values with tuples
def get_user_info():
    # Fetch user data from database
    return "John", 30, "john@example.com"

# Unpacking the returned tuple
name, age, email = get_user_info()""").scale(0.7)
            function_example.next_to(packing_example, DOWN, buff=0.5)
            self.play(Create(function_example))
        
        self.wait(1)
        self.play(FadeOut(packing_example), FadeOut(function_example))
        
        # Summary
        with self.voiceover(
            """
            Let's summarize the key differences between tuples and lists: 
            <bookmark mark='summary'/>
            
            Lists use square brackets, are mutable, and are best for collections that need to change. 
            <bookmark mark='summary_list'/>
            
            Tuples use parentheses, are immutable, have better performance, and can be used as dictionary keys. 
            <bookmark mark='summary_tuple'/>
            
            Choose the right data structure based on whether your data needs to change after creation. 
            <bookmark mark='summary_end'/>
            """
        ) as tracker:
            self.wait_until_bookmark("summary")
            
            self.play(Transform(syntax_title, Text("Summary", color=BLUE).scale(0.8).to_edge(UP)))
            
            summary_table = Table(
                [["Lists", "Tuples"],
                 ["[1, 2, 3]", "(1, 2, 3)"],
                 ["Mutable", "Immutable"],
                 ["Dynamic data", "Static data"],
                 ["Cannot be dict keys", "Can be dict keys"]],
                row_labels=[Text(""), Text("Syntax"), Text("Mutability"), 
                           Text("Use case"), Text("As keys")],
                include_outer_lines=True
            ).scale(0.55)
            
            # Position the summary table with proper centering and scaling
            summary_table.next_to(syntax_title, DOWN, buff=0.5)
            
            # Ensure the table is centered horizontally
            summary_table.move_to(ORIGIN + DOWN * 0.5)
            
            self.wait_until_bookmark("summary_list")
            self.play(Create(summary_table))
            
            self.wait_until_bookmark("summary_tuple")
            highlight_tuple = SurroundingRectangle(summary_table.get_columns()[1], color=YELLOW)
            self.play(Create(highlight_tuple))
            
            self.wait_until_bookmark("summary_end")
            self.play(FadeOut(highlight_tuple))
            highlight_all = SurroundingRectangle(summary_table, color=BLUE)
            self.play(Create(highlight_all))
        
        self.wait(1)
        
        # Conclusion
        with self.voiceover(
            """
            Thank you for watching this tutorial on tuples versus lists in Python!
            
            If you found this helpful, please like and subscribe for more Python tutorials.
            
            Happy coding!
            """
        ):
            # Clear all previous elements
            self.play(FadeOut(syntax_title), FadeOut(summary_table), FadeOut(highlight_all))
            
            # Create properly scaled conclusion elements
            final_title = Text("Tuples vs Lists in Python", color=YELLOW).scale(0.8)
            final_subtitle = Text("Choose the right tool for the job!", color=WHITE).scale(0.6)
            
            # Position elements in the center of the frame
            final_title.move_to(ORIGIN + UP * 0.5)
            final_subtitle.next_to(final_title, DOWN, buff=0.5)
            
            # Create a VGroup to ensure all elements are properly centered
            final_group = VGroup(final_title, final_subtitle)
            final_group.move_to(ORIGIN)
            
            # Animate the final elements
            self.play(Write(final_title))
            self.play(Write(final_subtitle))
        
        self.wait(2)
