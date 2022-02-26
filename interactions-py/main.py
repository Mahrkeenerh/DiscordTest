import interactions

TOKEN = open("TOKEN").readline()

bot = interactions.Client(token=TOKEN)

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
    scope=[889176263992963142]
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hello world!")


@bot.command(
    name="stop",
    description="Stop bot running",
    scope=[889176263992963142]
)
async def stop(ctx: interactions.CommandContext):
    await ctx.send("Bye!")
    # bot.stop()


@bot.command(
    name="say_something",
    description="say something!",
    scope=[889176263992963142],
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def say_something(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"You said '{text}'!")


@bot.command(
    name="base_command",
    description="This description isn't seen in UI (yet?)",
    scope=[889176263992963142],
    options=[
        interactions.Option(
            name="command_name",
            description="A descriptive description",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="option",
                    description="A descriptive description",
                    type=interactions.OptionType.INTEGER,
                    required=False,
                ),
            ],
        ),
        interactions.Option(
            name="second_command",
            description="A descriptive description",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="second_option",
                    description="A descriptive description",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
            ],
        ),
    ],
)
async def base_command(ctx: interactions.CommandContext, sub_command: str, second_option: str, option: int = None):
    if sub_command == "command_name":
      await ctx.send(f"You selected the command_name sub command and put in {option}")
    elif sub_command == "second_command":
      await ctx.send(f"You selected the second_command sub command and put in {second_option}")


@bot.command(
    type=interactions.ApplicationCommandType.USER,
    name="User Command",
    scope=[889176263992963142]
)
async def test(ctx):
    await ctx.send(f"You have applied a command onto user {ctx.target.user.username}!")


button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="hello world!",
    custom_id="hello"
)

@bot.command(
    name="button_test",
    description="This is the first command I made!",
    scope=[889176263992963142]
)
async def button_test(ctx):
    await ctx.send("testing", components=button)


@bot.component("hello")
async def button_response(ctx):
    await ctx.send("You clicked the Button :O", ephemeral=True)


button1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="hello world!",
    custom_id="hello",
)

button2 = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label="bye bye!",
    custom_id="bye!",
)


row = interactions.ActionRow(
    components=[button1, button2]
)
row2 = interactions.ActionRow(
    components=[button2, button1]
)

# NOT WORKING
@bot.command(
    name="button_test2",
    description="This is the first command I made!",
    scope=[889176263992963142]
)
async def test(ctx):
    await ctx.send("rows!", components=[row, row2])


embed_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="SEND EMBED",
    custom_id="send_embed"
)

@bot.command(
    name="send_embed_buttons",
    description="BUTTON EMBEDS",
    scope=[889176263992963142]
)
async def button_test(ctx):
    await ctx.send("Buttons and embeds", components=embed_button)

@bot.component("send_embed")
async def send_embed(ctx):
    embed_image = interactions.EmbedImageStruct(
        url="https://discord-py-slash-command.readthedocs.io/en/latest/_images/banner.png"
    )
    embed_something = interactions.EmbedField(
        name="field title",
        value="blah blah blah",
        inline=False,
    )
    await ctx.send("Sending this embeded picture", embeds=embed_something, ephemeral=True)


bot.start()
