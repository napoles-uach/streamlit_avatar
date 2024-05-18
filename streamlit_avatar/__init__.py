import streamlit as st
import streamlit.components.v1 as components

def avatar(text='', lang='en-US'):
    try:
        texto_usuario = text

        # Generación de los keyframes para la animación CSS.
        keyframes_waiting = """
            0% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_0.png'); }
            50% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_1.png'); }
            100% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_0.png'); }
        """

        keyframes_speaking = "".join([f"{i*10}% {{background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_{i}.png');}}\n" for i in range(10)])

        # Construcción del HTML para el avatar animado.
        html_str = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <title>Animated Speaking Avatar</title>
            <style>
                body {{
                    background: black;
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .avatar {{
                    width: 300px;
                    height: 300px;
                    background-size: cover;
                    animation: waitingAnimation 2s steps(2, end) infinite;
                }}
                @keyframes waitingAnimation {{
                    {keyframes_waiting}
                }}
                @keyframes speakAnimation {{
                    {keyframes_speaking}
                }}
            </style>
        </head>
        <body>
            <div class="avatar" id="avatar"></div>
            <script>
                document.addEventListener('DOMContentLoaded', (event) => {{
                    var avatar = document.getElementById("avatar");

                    var texto = `{texto_usuario}`;
                    var utterance = new SpeechSynthesisUtterance(texto);
                    utterance.lang = "{lang}"; // Configurar el idioma deseado
                    utterance.onstart = function(event) {{
                        avatar.style.animation = "speakAnimation 2s steps(5, end) infinite";
                    }};
                    utterance.onend = function(event) {{
                        setTimeout(() => {{ avatar.style.animation = "waitingAnimation 2s steps(2, end) infinite"; }}, 500);
                    }};
                    speechSynthesis.speak(utterance);
                }});
            </script>
        </body>
        </html>
        """

        # Renderizar el HTML en Streamlit
        components.html(html_str, height=300)
    except Exception as e:
        st.error(f"An error occurred: {e}")


        components.html(html_str, height=300)
    except:
        pass
