import streamlit as st

st.set_page_config(
    page_title="TeachBack",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% 20%, #101c2b 0%, #05070a 45%, #020305 100%);
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 5vh;
}

/* Main title */

.title {
    text-align: center;
    margin-top: 30px;
}

.title h1 {
    font-size: 72px;
    letter-spacing: 12px;
    margin-bottom: 5px;
    font-weight: 900;
    text-shadow:
        0 0 10px #00e5ff,
        0 0 30px rgba(0,229,255,0.4);
}

.version {
    color: #00e5ff;
    font-family: monospace;
    font-size: 13px;
    letter-spacing: 4px;
}

/* Tagline */

.tagline {
    text-align: center;
    margin-top: 25px;
    font-size: 28px;
    line-height: 1.5;
}

.tagline b {
    color: white;
}

/* How it works */

.how {
    max-width: 600px;
    margin: 50px auto 35px;
    padding: 28px 35px;

    background: rgba(10, 16, 24, 0.9);

    border: 1px solid #1d3947;
    border-radius: 14px;

    box-shadow:
        0 0 25px rgba(0,229,255,0.08),
        inset 0 0 20px rgba(0,229,255,0.03);
}

.how-title {
    color: #00e5ff;
    font-family: monospace;
    font-size: 13px;
    letter-spacing: 4px;
    margin-bottom: 22px;
}

.step {
    padding: 12px 10px;
    margin: 5px 0;

    font-family: monospace;
    font-size: 15px;

    color: #c9d1d9;

    border-left: 2px solid #00e5ff;

    background: rgba(0,229,255,0.025);
}

.step:hover {
    background: rgba(0,229,255,0.08);
    color: white;
}

/* Waiting text */

.waiting {
    text-align: center;
    color: #697586;
    font-family: monospace;
    letter-spacing: 2px;
    margin-top: 35px;
}

.learners {
    text-align: center;
    margin-top: 10px;

    color: #00e5ff;

    font-size: 19px;
    font-weight: 700;
    letter-spacing: 5px;

    text-shadow: 0 0 12px rgba(0,229,255,0.5);
}

/* Button */

.stButton {
    display: flex;
    justify-content: center;
}

.stButton > button {
    margin-top: 35px;

    padding: 14px 38px;

    border-radius: 8px;

    background: #07141b;
    color: #00e5ff;

    border: 1px solid #00e5ff;

    font-family: monospace;
    font-weight: bold;
    letter-spacing: 1px;

    box-shadow:
        0 0 10px rgba(0,229,255,0.2);

    transition: 0.2s;
}

.stButton > button:hover {
    background: #00e5ff;
    color: #020305;

    box-shadow:
        0 0 25px rgba(0,229,255,0.7);
}

</style>
""", unsafe_allow_html=True)


if "screen" not in st.session_state:
    st.session_state.screen = "intro"

if st.session_state.screen == "intro":

    st.html("""
    <div class="title">

    <h1>TEACHBACK</h1>

    <div class="version">
        LEARNING SYSTEM // v1.0
    </div>

</div>

<div class="tagline">

    <b>Don't learn from AI.</b><br>
    Teach it.

</div>

<div class="how">

    <div class="how-title">
        HOW IT WORKS
    </div>

    <div class="step">
        01 &nbsp; MEET YOUR LEARNER
    </div>

    <div class="step">
        02 &nbsp; FIND THE MISTAKE
    </div>

    <div class="step">
        03 &nbsp; TEACH THEM
    </div>

    <div class="step">
        04 &nbsp; TEST THEIR UNDERSTANDING
    </div>

</div>

<div class="waiting">
    YOUR LEARNERS ARE WAITING
</div>

<div class="learners">
    BYTE &nbsp; • &nbsp; NOVA &nbsp; • &nbsp; ECHO
    </div>
    """)




if "screen" not in st.session_state:
    st.session_state.screen = "intro"

if st.session_state.screen == "intro":

    
    if st.button("→ ENTER TEACHBACK", key="enter_teachback"):
        st.session_state.screen = "byte"
        st.rerun()

elif st.session_state.screen == "byte":

    st.html("""
    <div style="
        text-align:center;
        padding-top:60px;
    ">

        <div style="
            color:#00e5ff;
            font-family:monospace;
            letter-spacing:4px;
            font-size:14px;
        ">
            01 // MEET BYTE
        </div>

        <div style="
            margin-top:25px;
            font-size:60px;
            font-weight:900;
            letter-spacing:8px;
            color:white;
            text-shadow:
                0 0 12px #00e5ff,
                0 0 30px rgba(0,229,255,0.4);
        ">
            BYTE
        </div>

        <div style="
            margin-top:10px;
            color:#00e5ff;
            font-family:monospace;
            letter-spacing:3px;
        ">
            LEARNER // ONLINE
        </div>

        <div style="
            max-width:650px;
            margin:45px auto 0;
            padding:35px;

            background:rgba(10,16,24,0.9);
            border:1px solid #1d3947;
            border-radius:16px;

            box-shadow:
                0 0 30px rgba(0,229,255,0.08);
        ">

            <div style="
                font-size:28px;
                font-weight:700;
                margin-bottom:20px;
            ">
                “I'm still figuring things out.”
            </div>

            <div style="
                color:#aab4c0;
                font-size:16px;
                line-height:1.7;
            ">
                BYTE is curious, enthusiastic, and sometimes
                confidently confused.
                <br><br>
                They make simpler mistakes, misunderstand
                fundamentals, and aren't afraid to ask
                <i>“wait... why?”</i>
            </div>

        </div>

        <div style="
            margin-top:35px;
            color:#00e5ff;
            font-family:monospace;
            letter-spacing:3px;
            font-size:13px;
        ">
            YOUR ROLE
        </div>

        <div style="
            margin-top:10px;
            color:#c9d1d9;
            font-size:17px;
        ">
            Help BYTE build a stronger understanding.
        </div>

        <div style="
            margin-top:30px;
            font-family:monospace;
            color:#8b949e;
        ">
            LEARNER TYPE: BEGINNER
        </div>

    </div>
    """)

    if st.button("→ MEET BYTE", key="meet_byte"):
        st.session_state.screen = "nova"
        st.rerun()

elif st.session_state.screen == "nova":

    st.html("""
    <div style="
        text-align:center;
        padding-top:55px;
    ">

        <div style="
            color:#b56cff;
            font-family:monospace;
            letter-spacing:4px;
            font-size:14px;
        ">
            02 // MEET NOVA
        </div>

        <div style="
            margin-top:25px;
            font-size:60px;
            font-weight:900;
            letter-spacing:8px;
            color:white;
            text-shadow:
                0 0 12px #b56cff,
                0 0 35px rgba(181,108,255,0.45);
        ">
            NOVA
        </div>

        <div style="
            margin-top:10px;
            color:#b56cff;
            font-family:monospace;
            letter-spacing:3px;
        ">
            LEARNER // ONLINE
        </div>

        <div style="
            max-width:650px;
            margin:45px auto 0;
            padding:35px;

            background:rgba(15,10,25,0.92);
            border:1px solid #4b2868;
            border-radius:16px;

            box-shadow:
                0 0 35px rgba(181,108,255,0.12);
        ">

            <div style="
                font-size:28px;
                font-weight:700;
                margin-bottom:20px;
            ">
                “Come on. Prove me wrong.”
            </div>

            <div style="
                color:#bdb5c8;
                font-size:16px;
                line-height:1.7;
            ">
                NOVA is confident.
                <br><br>
                Sometimes <b>too confident.</b>
                <br><br>
                Their mistakes aren't always obvious.
                They can sound completely convincing while
                being fundamentally wrong.
            </div>

        </div>

        <div style="
            margin-top:35px;
            color:#b56cff;
            font-family:monospace;
            letter-spacing:3px;
            font-size:13px;
        ">
            YOUR ROLE
        </div>

        <div style="
            margin-top:10px;
            color:#d0c8d8;
            font-size:17px;
        ">
            Challenge NOVA. Find the flaw. Prove it.
        </div>

        <div style="
            margin-top:30px;
            font-family:monospace;
            color:#80758b;
        ">
            LEARNER TYPE: CONFIDENT
        </div>

    </div>
    """)

    if st.button("→ MEET NOVA", key="meet_nova"):
        st.session_state.screen = "echo"
        st.rerun()

elif st.session_state.screen == "echo":

    st.html("""
    <div style="
        text-align:center;
        padding-top:55px;
        background:
            radial-gradient(
                circle at 50% 20%,
                rgba(30,30,40,0.35),
                transparent 55%
            );
    ">

        <div style="
            color:#9da3ad;
            font-family:monospace;
            letter-spacing:4px;
            font-size:14px;
        ">
            03 // MEET ECHO
        </div>

        <div style="
            margin-top:25px;
            font-size:60px;
            font-weight:900;
            letter-spacing:10px;
            color:#e6e6e6;
            text-shadow:
                0 0 10px rgba(255,255,255,0.15);
        ">
            ECHO
        </div>

        <div style="
            margin-top:10px;
            color:#8b929c;
            font-family:monospace;
            letter-spacing:3px;
        ">
            LEARNER // ONLINE
        </div>

        <div style="
            max-width:650px;
            margin:45px auto 0;
            padding:35px;

            background:rgba(5,6,8,0.96);
            border:1px solid #343942;
            border-radius:10px;

            box-shadow:
                0 0 40px rgba(0,0,0,0.45);
        ">

            <div style="
                font-size:28px;
                font-weight:700;
                margin-bottom:20px;
                color:#eeeeee;
            ">
                “I know the theory. Test my reasoning.”
            </div>

            <div style="
                color:#9da3ad;
                font-size:16px;
                line-height:1.8;
            ">
                ECHO doesn't make obvious mistakes.
                <br><br>
                It remembers definitions and patterns —
                but struggles when the problem changes.
                <br><br>
                Knowing something isn't always the same
                as being able to apply it.
            </div>

        </div>

        <div style="
            margin-top:35px;
            color:#aeb4bd;
            font-family:monospace;
            letter-spacing:3px;
            font-size:13px;
        ">
            YOUR ROLE
        </div>

        <div style="
            margin-top:10px;
            color:#c5c9cf;
            font-size:17px;
        ">
            Go beyond memorization. Test whether ECHO
            can actually apply what it knows.
        </div>

        <div style="
            margin-top:30px;
            font-family:monospace;
            color:#737983;
        ">
            LEARNER TYPE: ANALYTICAL
        </div>

    </div>
    """)

    if st.button("→ CHOOSE YOUR LEARNER", key="choose_learner"):
        st.session_state.screen = "choose"
        st.rerun()

elif st.session_state.screen == "choose":

    st.html("""
    <div style="
        text-align:center;
        padding-top:45px;
    ">

        <div style="
            color:#00e5ff;
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            SELECT YOUR LEARNER
        </div>

        <div style="
            margin-top:18px;
            font-size:42px;
            font-weight:900;
            letter-spacing:5px;
            color:white;
            text-shadow:0 0 18px rgba(0,229,255,0.35);
        ">
            CHOOSE YOUR LEARNER
        </div>

        <div style="
            margin-top:12px;
            color:#7f8b98;
            font-family:monospace;
            font-size:14px;
        ">
            THREE MINDS. THREE DIFFERENT CHALLENGES.
        </div>

    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.html("""
        <div style="
            margin-top:35px;
            padding:28px;
            background:rgba(7,18,27,0.92);
            border:1px solid #00e5ff;
            border-radius:14px;
            text-align:center;
            box-shadow:0 0 25px rgba(0,229,255,0.08);
        ">
            <div style="
                color:#00e5ff;
                font-family:monospace;
                letter-spacing:3px;
                font-size:12px;
            ">
                01
            </div>

            <div style="
                margin-top:12px;
                font-size:38px;
                font-weight:900;
                letter-spacing:6px;
                color:white;
                text-shadow:0 0 12px #00e5ff;
            ">
                BYTE
            </div>

            <div style="
                margin-top:8px;
                color:#00e5ff;
                font-family:monospace;
                font-size:12px;
            ">
                BEGINNER
            </div>

            <div style="
                margin-top:20px;
                color:#9daab5;
                line-height:1.6;
                font-size:14px;
            ">
                Curious. Enthusiastic.<br>
                Sometimes confidently confused.
            </div>
        </div>
        """)

        if st.button("→ SELECT BYTE", key="select_byte"):
            st.session_state.learner = "byte"
            st.session_state.screen = "mission"
            st.rerun()

    with col2:
        st.html("""
        <div style="
            margin-top:35px;
            padding:28px;
            background:rgba(20,10,30,0.92);
            border:1px solid #b56cff;
            border-radius:14px;
            text-align:center;
            box-shadow:0 0 25px rgba(181,108,255,0.10);
        ">
            <div style="
                color:#b56cff;
                font-family:monospace;
                letter-spacing:3px;
                font-size:12px;
            ">
                02
            </div>

            <div style="
                margin-top:12px;
                font-size:38px;
                font-weight:900;
                letter-spacing:6px;
                color:white;
                text-shadow:0 0 12px #b56cff;
            ">
                NOVA
            </div>

            <div style="
                margin-top:8px;
                color:#b56cff;
                font-family:monospace;
                font-size:12px;
            ">
                CONFIDENT
            </div>

            <div style="
                margin-top:20px;
                color:#bdb5c8;
                line-height:1.6;
                font-size:14px;
            ">
                Confident. Convincing.<br>
                Not always correct.
            </div>
        </div>
        """)

        if st.button("→ SELECT NOVA", key="select_nova"):
            st.session_state.learner = "nova"
            st.session_state.screen = "mission"
            st.rerun()

    st.html("""
    <div style="
        width:48%;
        margin:25px auto 0;
        padding:28px;
        background:rgba(5,6,8,0.96);
        border:1px solid #444a52;
        border-radius:14px;
        text-align:center;
        box-shadow:0 0 30px rgba(0,0,0,0.4);
    ">
        <div style="
            color:#858b94;
            font-family:monospace;
            letter-spacing:3px;
            font-size:12px;
        ">
            03
        </div>

        <div style="
            margin-top:12px;
            font-size:38px;
            font-weight:900;
            letter-spacing:7px;
            color:#e8e8e8;
        ">
            ECHO
        </div>

        <div style="
            margin-top:8px;
            color:#858b94;
            font-family:monospace;
            font-size:12px;
        ">
            ANALYTICAL
        </div>

        <div style="
            margin-top:20px;
            color:#9da3ad;
            line-height:1.6;
            font-size:14px;
        ">
            Remembers the theory.<br>
            Struggles when the problem changes.
        </div>
    </div>
    """)

    if st.button("→ SELECT ECHO", key="select_echo"):
        st.session_state.learner = "echo"
        st.session_state.screen = "mission"
        st.rerun()

elif st.session_state.screen == "mission":

    learner = st.session_state.get("learner", "byte")

    names = {
        "byte": "BYTE",
        "nova": "NOVA",
        "echo": "ECHO"
    }

    colors = {
        "byte": "#00e5ff",
        "nova": "#b56cff",
        "echo": "#9da3ad"
    }

    quotes = {
        "byte": '"Okay... I\'m ready! I think."',
        "nova": '"Let\'s see if you can actually challenge me."',
        "echo": '"Learning protocol initialized."'
    }

    name = names[learner]
    color = colors[learner]
    quote = quotes[learner]

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:60px;
    ">

        <div style="
            color:{color};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 01 // INITIALIZATION
        </div>

        <div style="
            margin-top:25px;
            font-size:20px;
            color:#7f8b98;
            font-family:monospace;
            letter-spacing:2px;
        ">
            LEARNER SELECTED
        </div>

        <div style="
            margin-top:10px;
            font-size:64px;
            font-weight:900;
            letter-spacing:9px;
            color:white;
            text-shadow:0 0 18px {color};
        ">
            {name}
        </div>

        <div style="
            max-width:600px;
            margin:45px auto;
            padding:35px;

            background:rgba(8,12,17,0.94);
            border:1px solid {color};
            border-radius:15px;

            box-shadow:0 0 30px rgba(0,0,0,0.35);
        ">

            <div style="
                font-size:25px;
                font-weight:700;
            ">
                {quote}
            </div>

            <div style="
                margin-top:25px;
                color:#9da6b0;
                line-height:1.7;
                font-size:15px;
            ">
                Your first mission is about to begin.
                <br>
                Find the misunderstanding.
                <br>
                Explain what went wrong.
                <br>
                Then prove that your learner understands.
            </div>

        </div>

        <div style="
            color:{color};
            font-family:monospace;
            letter-spacing:3px;
            font-size:13px;
        ">
            MISSION STATUS // READY
        </div>

    </div>
    """)

    if st.button("→ START MISSION", key="start_mission"):
        st.session_state.screen = "challenge"
        st.rerun()

elif st.session_state.screen == "challenge":

    learner = st.session_state.get("learner", "byte")

    challenges = {
        "byte": {
            "name": "BYTE",
            "color": "#00e5ff",
            "question": "In Python, what will this code print?",
            "code": "x = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
            "response": '"The answer is [1, 2, 3] because I only changed y, not x."',
            "choices": [
                "The learner thinks y creates a completely separate list.",
                "The learner thinks append() only changes the last variable used.",
                "The learner thinks Python lists cannot be modified.",
                "There is no mistake — the learner is correct."
            ]
        },

        "nova": {
            "name": "NOVA",
            "color": "#b56cff",
            "question": "A program checks whether a number is even. What is wrong with this reasoning?",
            "code": "n = 7\nif n / 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
            "response": '"7 divided by 2 is not zero, so the program correctly prints Odd. The condition is fine."',
            "choices": [
                "NOVA confuses division with checking the remainder.",
                "NOVA thinks if statements cannot compare numbers.",
                "NOVA thinks 7 is actually an even number.",
                "There is no mistake — NOVA is correct."
            ]
        },

        "echo": {
            "name": "ECHO",
            "color": "#9da3ad",
            "question": "A function is supposed to change the original list. What is wrong?",
            "code": "def add_item(items):\n    items = items + [4]\n\nnums = [1, 2, 3]\nadd_item(nums)\nprint(nums)",
            "response": '"The function adds 4 to items, so nums should now contain 4 as well."',
            "choices": [
                "ECHO assumes changing the local variable changes the original list.",
                "ECHO thinks functions cannot receive lists.",
                "ECHO thinks + can only be used with numbers.",
                "There is no mistake — ECHO is correct."
            ]
        }
    }

    data = challenges[learner]

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:35px;
    ">

        <div style="
            color:{data['color']};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 01 // FIND THE MISTAKE
        </div>

        <div style="
            margin-top:18px;
            font-size:42px;
            font-weight:900;
            letter-spacing:6px;
            color:white;
        ">
            {data['name']}
        </div>

    </div>

    <div style="
        max-width:760px;
        margin:35px auto 25px;
        padding:30px;

        background:rgba(8,12,17,0.94);
        border:1px solid #26313d;
        border-radius:16px;
    ">

        <div style="
            color:{data['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            LEARNER RESPONSE
        </div>

        <div style="
            margin-top:18px;
            font-size:20px;
            line-height:1.7;
            color:#e8edf2;
        ">
            {data['question']}
        </div>

        <pre style="
            margin-top:20px;
            padding:18px;
            background:#05070a;
            border-radius:8px;
            color:#d8dee6;
            text-align:left;
        ">{data['code']}</pre>

        <div style="
            margin-top:20px;
            padding:18px;
            background:#111820;
            border-left:3px solid {data['color']};
            color:#b9c3cc;
            line-height:1.6;
        ">
            {data['name']} says:
            <br><br>
            <strong style="color:white;">
                {data['response']}
            </strong>
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:30px auto 18px;
        padding:22px;
        text-align:center;

        background:rgba(0,229,255,0.06);
        border:1px solid {data['color']};
        border-radius:12px;

        box-shadow:0 0 20px rgba(0,229,255,0.08);
    ">

        <div style="
            color:{data['color']};
            font-family:monospace;
            font-size:13px;
            letter-spacing:3px;
            font-weight:bold;
        ">
            YOUR OBJECTIVE
        </div>

        <div style="
            margin-top:8px;
            font-size:27px;
            font-weight:900;
            color:white;
        ">
            WHAT WENT WRONG?
        </div>

        <div style="
            margin-top:6px;
            color:#aab4c0;
            font-size:14px;
        ">
            Identify the learner's misconception.
        </div>

    </div>
    """)

    mistake = st.radio(
        "Select the diagnosis:",
        data["choices"],
        key="mission1_mistake"
    )

    if st.button("→ ANALYZE RESPONSE", key="analyze_mission1"):

        st.session_state.mission1_answer = mistake
        st.session_state.screen = "feedback"
        st.rerun()


elif st.session_state.screen == "feedback":

    learner = st.session_state.get("learner", "byte")
    answer = st.session_state.get("mission1_answer", "")

    correct_answers = {
        "byte": "The learner thinks y creates a completely separate list.",
        "nova": "NOVA confuses division with checking the remainder.",
        "echo": "ECHO assumes changing the local variable changes the original list."
    }

    explanations = {
        "byte": {
            "title": "LIST REFERENCES",
            "text": "In Python, assigning y = x does not create a new list. Both variables refer to the same list. So when y.append(4) changes the list, x also shows the new value.",
            "mistake": "The learner treated y as an independent copy of x.",
            "fix": "To create a separate list, use x.copy() or x[:]."
        },

        "nova": {
            "title": "REMAINDER VS DIVISION",
            "text": "Division tells you the result of dividing two numbers. To check whether a number is even, we need to check its remainder after division by 2.",
            "mistake": "NOVA used / instead of the modulo operator %.",
            "fix": "Use n % 2 == 0 to check whether n is even."
        },

        "echo": {
            "title": "LOCAL VARIABLES",
            "text": "Inside the function, items = items + [4] creates a new list and assigns it to the local variable items. The original nums list is never changed.",
            "mistake": "ECHO confused changing a local variable with modifying the original object.",
            "fix": "Use items.append(4) if the goal is to modify the original list."
        }
    }

    is_correct = answer == correct_answers[learner]
    data = explanations[learner]

    color = {
        "byte": "#00e5ff",
        "nova": "#b56cff",
        "echo": "#9da3ad"
    }[learner]

    status = "DIAGNOSIS CORRECT" if is_correct else "DIAGNOSIS INCORRECT"
    status_color = "#00ff9d" if is_correct else "#ff5577"

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:40px;
    ">

        <div style="
            color:{color};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 01 // ANALYSIS
        </div>

        <div style="
            margin-top:18px;
            font-size:40px;
            font-weight:900;
            letter-spacing:5px;
            color:white;
        ">
            RESPONSE ANALYZED
        </div>

        <div style="
            margin-top:18px;
            color:{status_color};
            font-family:monospace;
            font-size:15px;
            letter-spacing:3px;
            font-weight:bold;
        ">
            {status}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:35px auto 20px;
        padding:28px;

        background:rgba(8,12,17,0.95);
        border:1px solid {status_color};
        border-radius:16px;
    ">

        <div style="
            color:{color};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            WHAT ACTUALLY WENT WRONG
        </div>

        <div style="
            margin-top:15px;
            font-size:24px;
            font-weight:800;
            color:white;
        ">
            {data['title']}
        </div>

        <div style="
            margin-top:18px;
            color:#c1c9d2;
            line-height:1.7;
            font-size:16px;
        ">
            {data['text']}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:20px auto;
        padding:24px;

        background:#10161d;
        border-radius:14px;
        border-left:3px solid {color};
    ">

        <div style="
            color:{color};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            THE MISCONCEPTION
        </div>

        <div style="
            margin-top:12px;
            color:white;
            font-size:17px;
            line-height:1.6;
        ">
            {data['mistake']}
        </div>

        <div style="
            margin-top:22px;
            color:{color};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            HOW TO FIX IT
        </div>

        <div style="
            margin-top:10px;
            color:#c1c9d2;
            font-size:16px;
            line-height:1.6;
        ">
            {data['fix']}
        </div>

    </div>
    """)

    if st.button("→ CONTINUE", key="continue_mission1"):
            st.session_state.screen = "next_mission"
            st.rerun()
    
elif st.session_state.screen == "next_mission":

    learner = st.session_state.get("learner", "byte")

    data = {
        "byte": {
            "name": "BYTE",
            "color": "#00e5ff",
            "topic": "PYTHON LISTS",
            "prompt": "BYTE keeps confusing a list with a copy of a list.",
            "question": "How would you explain this to BYTE?",
            "options": [
                "A variable can point to the same list as another variable. Changing the list affects both.",
                "Every variable automatically creates a new copy of the data.",
                "Python lists cannot be changed after they are created.",
                "The second variable is always deleted when the first changes."
            ],
            "correct": 0
        },

        "nova": {
            "name": "NOVA",
            "color": "#b56cff",
            "topic": "MODULO OPERATOR",
            "prompt": "NOVA knows division, but keeps using it when checking whether numbers are even or odd.",
            "question": "Which explanation would actually correct NOVA?",
            "options": [
                "Use / because it tells Python whether a number is even.",
                "Use % because it gives the remainder after division.",
                "Use * because even numbers are multiples of two.",
                "Use // because it checks whether a number is divisible."
            ],
            "correct": 1
        },

        "echo": {
            "name": "ECHO",
            "color": "#9da3ad",
            "topic": "FUNCTIONS & MUTABILITY",
            "prompt": "ECHO understands functions, but assumes every assignment inside a function changes the original variable.",
            "question": "What explanation would make the distinction clear?",
            "options": [
                "Every variable inside a function automatically changes the outside variable.",
                "Functions cannot modify lists.",
                "Reassigning a local variable is different from modifying the object it refers to.",
                "Python creates a new function every time a variable is reassigned."
            ],
            "correct": 2
        }
    }

    mission = data[learner]

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:35px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 02 // TEACH THE LEARNER
        </div>

        <div style="
            margin-top:18px;
            font-size:40px;
            font-weight:900;
            letter-spacing:5px;
            color:white;
        ">
            {mission['name']}
        </div>

        <div style="
            margin-top:10px;
            color:#87929e;
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            TOPIC // {mission['topic']}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:35px auto 25px;
        padding:28px;

        background:rgba(8,12,17,0.95);
        border:1px solid #26313d;
        border-radius:16px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            THE LEARNER IS STUCK
        </div>

        <div style="
            margin-top:16px;
            color:#e5eaf0;
            font-size:18px;
            line-height:1.7;
        ">
            {mission['prompt']}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:25px auto 18px;
        padding:22px;

        background:rgba(0,229,255,0.05);
        border:1px solid {mission['color']};
        border-radius:12px;
        text-align:center;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:3px;
            font-weight:bold;
        ">
            YOUR TEACHING TASK
        </div>

        <div style="
            margin-top:10px;
            color:white;
            font-size:23px;
            font-weight:800;
        ">
            {mission['question']}
        </div>

    </div>
    """)

    teaching = st.radio(
        "Choose your explanation:",
        mission["options"],
        key="mission2_teaching"
    )

    if st.button("→ TEACH {0}".format(mission["name"]), key="teach_mission2"):

        selected_index = mission["options"].index(teaching)

        st.session_state.mission2_correct = (
            selected_index == mission["correct"]
        )

        st.session_state.screen = "teaching_feedback"
        st.rerun()

elif st.session_state.screen == "teaching_feedback":

    learner = st.session_state.get("learner", "byte")
    correct = st.session_state.get("mission2_correct", False)

    data = {
        "byte": {
            "name": "BYTE",
            "color": "#00e5ff",
            "topic": "LIST REFERENCES",
            "correct_title": "BYTE GETS IT NOW",
            "correct_text": "Your explanation correctly showed that two variables can refer to the same list. That is the key idea BYTE was missing.",
            "wrong_title": "BYTE IS STILL CONFUSED",
            "wrong_text": "Your explanation missed the main issue: assigning another variable does not automatically create a separate copy of a list.",
            "next": "Remember: two variables can point to the same object."
        },

        "nova": {
            "name": "NOVA",
            "color": "#b56cff",
            "topic": "MODULO OPERATOR",
            "correct_title": "NOVA HAS BEEN CHALLENGED",
            "correct_text": "You correctly explained that % gives the remainder after division. That is exactly what NOVA needs to distinguish even and odd numbers.",
            "wrong_title": "NOVA STILL HAS A POINT",
            "wrong_text": "Your explanation did not address the actual problem. The key is checking the remainder, not the result of normal division.",
            "next": "Remember: n % 2 == 0 means there is no remainder."
        },

        "echo": {
            "name": "ECHO",
            "color": "#9da3ad",
            "topic": "LOCAL VARIABLES",
            "correct_title": "ECHO UNDERSTANDS THE DISTINCTION",
            "correct_text": "You correctly separated reassignment from modification. A local variable can be redirected to a new object without changing the original object.",
            "wrong_title": "ECHO NEEDS MORE CLARITY",
            "wrong_text": "Your explanation mixed up the local variable with the original object. Reassigning a variable is not the same as modifying the object it refers to.",
            "next": "Remember: changing a reference and changing an object are different operations."
        }
    }

    mission = data[learner]

    if correct:
        title = mission["correct_title"]
        text = mission["correct_text"]
        status = "TEACHING SUCCESSFUL"
        status_color = "#00ff9d"
    else:
        title = mission["wrong_title"]
        text = mission["wrong_text"]
        status = "TEACHING NEEDS WORK"
        status_color = "#ff5577"

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:40px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 02 // FEEDBACK
        </div>

        <div style="
            margin-top:18px;
            font-size:40px;
            font-weight:900;
            letter-spacing:5px;
            color:white;
        ">
            TEACHING ANALYZED
        </div>

        <div style="
            margin-top:16px;
            color:{status_color};
            font-family:monospace;
            font-size:14px;
            letter-spacing:3px;
            font-weight:bold;
        ">
            {status}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:35px auto 20px;
        padding:30px;

        background:rgba(8,12,17,0.95);
        border:1px solid {status_color};
        border-radius:16px;
        box-shadow:0 0 25px rgba(0,0,0,0.25);
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            {mission['name']} // {mission['topic']}
        </div>

        <div style="
            margin-top:16px;
            font-size:25px;
            font-weight:800;
            color:white;
        ">
            {title}
        </div>

        <div style="
            margin-top:16px;
            color:#c3ccd5;
            font-size:16px;
            line-height:1.7;
        ">
            {text}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:20px auto;
        padding:22px;

        background:#10161d;
        border-left:3px solid {mission['color']};
        border-radius:12px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            KEY TAKEAWAY
        </div>

        <div style="
            margin-top:10px;
            color:white;
            font-size:17px;
            line-height:1.6;
        ">
            {mission['next']}
        </div>

    </div>
    """)

    if st.button("→ CONTINUE TO MISSION 03", key="continue_mission2"):
        st.session_state.screen = "mission3"
        st.rerun()
elif st.session_state.screen == "mission3":

    learner = st.session_state.get("learner", "byte")

    data = {
        "byte": {
            "name": "BYTE",
            "color": "#00e5ff",
            "topic": "LIST REFERENCES",
            "situation": "BYTE now says: \"If I use x.copy(), then changing y will still change x because both contain the same values.\"",
            "choices": [
                "BYTE understands the concept correctly.",
                "BYTE is still confusing shared references with copied values.",
                "BYTE is confusing lists with strings."
            ],
            "correct": 1
        },

        "nova": {
            "name": "NOVA",
            "color": "#b56cff",
            "topic": "MODULO",
            "situation": "NOVA says: \"12 is even because 12 / 2 gives 6, so checking n % 2 isn't really necessary.\"",
            "choices": [
                "NOVA completely understands the concept.",
                "NOVA is still confusing division with checking a remainder.",
                "NOVA is confusing even numbers with negative numbers."
            ],
            "correct": 1
        },

        "echo": {
            "name": "ECHO",
            "color": "#9da3ad",
            "topic": "FUNCTIONS",
            "situation": "ECHO says: \"If I write items = items + [4] inside the function, the original list must change because items came from that list.\"",
            "choices": [
                "ECHO understands the difference between reassignment and modification.",
                "ECHO is still confusing a local reassignment with modifying the original object.",
                "ECHO is confusing functions with loops."
            ],
            "correct": 1
        }
    }

    mission = data[learner]

    st.html(f"""
    <div style="
        text-align:center;
        padding-top:40px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            MISSION 03 // FINAL TEST
        </div>

        <div style="
            margin-top:18px;
            font-size:42px;
            font-weight:900;
            letter-spacing:6px;
            color:white;
        ">
            DID THEY LEARN?
        </div>

        <div style="
            margin-top:10px;
            color:#7f8b98;
            font-family:monospace;
            letter-spacing:2px;
            font-size:12px;
        ">
            SAME CONCEPT // NEW SITUATION
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:40px auto 25px;
        padding:30px;

        background:rgba(8,12,17,0.95);
        border:1px solid {mission['color']};
        border-radius:16px;

        box-shadow:0 0 25px rgba(0,0,0,0.3);
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            {mission['name']} // NEW RESPONSE
        </div>

        <div style="
            margin-top:20px;
            font-size:20px;
            line-height:1.8;
            color:#e5eaf0;
        ">
            {mission['situation']}
        </div>

    </div>
    """)

    st.html(f"""
    <div style="
        max-width:760px;
        margin:25px auto 18px;
        padding:22px;
        text-align:center;

        background:rgba(0,229,255,0.05);
        border:1px solid {mission['color']};
        border-radius:12px;
    ">

        <div style="
            color:{mission['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:3px;
            font-weight:bold;
        ">
            FINAL DIAGNOSIS
        </div>

        <div style="
            margin-top:9px;
            color:white;
            font-size:23px;
            font-weight:900;
        ">
            Has {mission['name']} actually understood?
        </div>

    </div>
    """)

    final_choice = st.radio(
        "Choose your diagnosis:",
        mission["choices"],
        key="mission3_choice"
    )

    if st.button("→ SUBMIT FINAL DIAGNOSIS", key="submit_mission3"):

        selected = mission["choices"].index(final_choice)

        st.session_state.mission3_correct = (
            selected == mission["correct"]
        )

        st.session_state.screen = "final_profile"
        st.rerun()
elif st.session_state.screen == "final_profile":

    learner = st.session_state.get("learner", "byte")

    profiles = {
        "byte": {
            "name": "BYTE",
            "color": "#00e5ff",
            "type": "THE BEGINNER",
            "line": "Curious, enthusiastic, still building the fundamentals.",
            "learned": "You worked on how Python variables can refer to the same list, and why copying a list is different from sharing a reference."
        },
        "nova": {
            "name": "NOVA",
            "color": "#b56cff",
            "type": "THE CONFIDENT ONE",
            "line": "Confident, challenging, and sometimes too sure.",
            "learned": "You worked on the difference between division and the modulo operator, especially when checking whether a number is even or odd."
        },
        "echo": {
            "name": "ECHO",
            "color": "#9da3ad",
            "type": "THE ANALYTICAL ONE",
            "line": "Knows the theory. Now learning to apply it.",
            "learned": "You worked on the difference between changing a local variable and actually modifying the original object."
        }
    }

    p = profiles[learner]

    m1 = st.session_state.get("mission1_answer", "")
    m2 = st.session_state.get("mission2_correct", False)
    m3 = st.session_state.get("mission3_correct", False)

    correct1 = {
        "byte": "The learner thinks y creates a completely separate list.",
        "nova": "NOVA confuses division with checking the remainder.",
        "echo": "ECHO assumes changing the local variable changes the original list."
    }

    score = 0

    if m1 == correct1[learner]:
        score += 1

    if m2:
        score += 1

    if m3:
        score += 1

    percent = round((score / 3) * 100)

    if percent == 100:
        result = "UNDERSTANDING CONFIRMED"
        explanation = "You successfully identified the misconception, explained the concept, and recognized whether the learner understood it."
    elif percent >= 67:
        result = "STRONG PROGRESS"
        explanation = "You identified most of the learning issue correctly. The core idea is there, but one part could still use a little reinforcement."
    elif percent >= 33:
        result = "PARTIAL UNDERSTANDING"
        explanation = "You caught part of the misconception, but some of the reasoning still needs reinforcement. Focus on the exact difference between the concepts."
    else:
        result = "MORE PRACTICE NEEDED"
        explanation = "The misconception was difficult to identify this time. Review the explanation and try applying the concept to a new example."

    # HEADER
    st.html(f"""
    <div style="
        text-align:center;
        padding-top:35px;
    ">

        <div style="
            color:{p['color']};
            font-family:monospace;
            letter-spacing:4px;
            font-size:13px;
        ">
            TEACHBACK // SESSION COMPLETE
        </div>

        <div style="
            margin-top:18px;
            font-size:42px;
            font-weight:900;
            letter-spacing:5px;
            color:white;
            text-shadow:0 0 18px {p['color']}55;
        ">
            PROFILE COMPLETE
        </div>

        <div style="
            margin-top:10px;
            color:#7f8b98;
            font-family:monospace;
            font-size:14px;
        ">
            LEARNING SESSION ANALYZED
        </div>

    </div>
    """)

    # PROFILE CARD
    st.html(f"""
    <div style="
        margin-top:35px;
        padding:25px;
        border:1px solid {p['color']}55;
        border-radius:14px;
        background:linear-gradient(
            135deg,
            {p['color']}0d,
            rgba(255,255,255,0.02)
        );
        box-shadow:0 0 25px {p['color']}12;
    ">

        <div style="
            color:{p['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:3px;
        ">
            LEARNER PROFILE
        </div>

        <div style="
            margin-top:10px;
            font-size:30px;
            font-weight:800;
            color:white;
        ">
            {p['name']}
        </div>

        <div style="
            margin-top:4px;
            color:{p['color']};
            font-family:monospace;
            font-size:13px;
            letter-spacing:2px;
        ">
            {p['type']}
        </div>

        <div style="
            margin-top:14px;
            color:#aab3bd;
            font-size:14px;
        ">
            {p['line']}
        </div>

    </div>
    """)

    # SCORE
    st.html(f"""
    <div style="
        margin-top:25px;
        padding:25px;
        text-align:center;
        border:1px solid #ffffff18;
        border-radius:14px;
        background:#080b10;
    ">

        <div style="
            color:#7f8b98;
            font-family:monospace;
            font-size:12px;
            letter-spacing:3px;
        ">
            TEACHING SCORE
        </div>

        <div style="
            margin-top:8px;
            font-size:58px;
            font-weight:900;
            color:{p['color']};
            text-shadow:0 0 20px {p['color']}55;
        ">
            {percent}%
        </div>

        <div style="
            color:#8d98a5;
            font-family:monospace;
            font-size:13px;
        ">
            {score} / 3 MISSIONS PASSED
        </div>

    </div>
    """)

    # MISSION RESULTS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "MISSION 01",
            "PASSED" if m1 == correct1[learner] else "MISSED"
        )

    with col2:
        st.metric(
            "MISSION 02",
            "PASSED" if m2 else "MISSED"
        )

    with col3:
        st.metric(
            "MISSION 03",
            "PASSED" if m3 else "MISSED"
        )

    # EXPLANATION BOX
    st.html(f"""
    <div style="
        margin-top:25px;
        padding:22px;
        border-left:3px solid {p['color']};
        border-radius:10px;
        background:{p['color']}0a;
    ">

        <div style="
            color:{p['color']};
            font-family:monospace;
            font-size:12px;
            letter-spacing:2px;
        ">
            WHAT THIS MEANS
        </div>

        <div style="
            margin-top:10px;
            font-size:22px;
            font-weight:800;
            color:white;
        ">
            {result}
        </div>

        <div style="
            margin-top:8px;
            color:#aab3bd;
            font-size:14px;
            line-height:1.6;
        ">
            {explanation}
        </div>

    </div>
    """)

    # WHAT YOU LEARNED
    st.html(f"""
    <div style="
        margin-top:18px;
        padding:20px;
        border:1px solid #ffffff14;
        border-radius:10px;
        background:#080b10;
    ">

        <div style="
            color:#7f8b98;
            font-family:monospace;
            font-size:11px;
            letter-spacing:2px;
        ">
            WHAT YOU LEARNED
        </div>

        <div style="
            margin-top:9px;
            color:#d7dde3;
            font-size:14px;
            line-height:1.6;
        ">
            {p['learned']}
        </div>

    </div>
    """)

    # FOOTER
    st.html("""
    <div style="
        text-align:center;
        margin-top:35px;
        padding-bottom:20px;
        color:#46515d;
        font-family:monospace;
        font-size:11px;
        letter-spacing:2px;
    ">
        TEACHBACK // LEARNING THROUGH TEACHING
    </div>
    """)