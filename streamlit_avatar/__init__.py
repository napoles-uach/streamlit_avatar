import streamlit as st
import streamlit.components.v1 as components

def avatar(text='', lang='en-US'):
    try:
        texto_usuario = text

        # Generación de los keyframes para la animación CSS.
        keyframes_waiting = """
            0% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_1.png'); }
            50% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_1.png'); }
            100% { background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_closed_eyes.png'); }
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
                    background: white;
                    color: black;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    overflow: hidden;
                }}
                .avatar {{
                    width: 300px;
                    height: 300px;
                    background-size: cover;
                    animation: waitingAnimation 2s steps(2, end) infinite;
                    z-index: 1;
                }}
                @keyframes waitingAnimation {{
                    {keyframes_waiting}
                }}
                @keyframes speakAnimation {{
                    {keyframes_speaking}
                }}
                .snowflake {{
                    position: absolute;
                    top: -10px;
                    width: 10px;
                    height: 10px;
                    background: white;
                    border-radius: 50%;
                    opacity: 0.8;
                    animation: fall linear infinite;
                    z-index: 2;
                }}
                @keyframes fall {{
                    0% {{ transform: translateY(0); opacity: 0.8; }}
                    100% {{ transform: translateY(100vh); opacity: 0.2; }}
                }}
            </style>
        </head>
        <body>
            <div id="snowflakes"></div>
            <div class="avatar" id="avatar"></div>
            <script>
                document.addEventListener('DOMContentLoaded', (event) => {{
                    var avatar = document.getElementById("avatar");

                    function setAnimation(animationName, duration, steps) {{
                        avatar.style.animation = 'none'; // Detener la animación actual
                        void avatar.offsetWidth; // Reiniciar el flujo de CSS
                        avatar.style.animation = `${{animationName}} ${{duration}}s steps(${{steps}}, end) infinite`;
                    }}

                    var texto = `{texto_usuario}`;
                    var utterance = new SpeechSynthesisUtterance(texto);
                    utterance.lang = "{lang}"; // Configurar el idioma deseado
                    utterance.onstart = function(event) {{
                        setAnimation('speakAnimation', 2, 10);
                    }};
                    utterance.onend = function(event) {{
                        setTimeout(() => {{ setAnimation('waitingAnimation', 2, 2); }}, 500);
                    }};
                    speechSynthesis.speak(utterance);

                    // Crear copos de nieve
                    function createSnowflake() {{
                        var snowflake = document.createElement("div");
                        snowflake.classList.add("snowflake");
                        snowflake.style.left = Math.random() * 100 + "vw";
                        snowflake.style.animationDuration = (Math.random() * 5 + 5) + "s";
                        snowflake.style.width = (Math.random() * 5 + 5) + "px";
                        snowflake.style.height = snowflake.style.width;
                        document.getElementById("snowflakes").appendChild(snowflake);

                        // Eliminar copo de nieve después de que caiga
                        setTimeout(() => {{
                            snowflake.remove();
                        }}, parseFloat(snowflake.style.animationDuration) * 1000);
                    }}

                    // Crear múltiples copos de nieve
                    setInterval(createSnowflake, 200);
                }});
            </script>
        </body>
        </html>
        """

        # Renderizar el HTML en Streamlit
        components.html(html_str, height=600)
    except Exception as e:
        st.error(f"An error occurred: {e}")
