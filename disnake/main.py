import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True

# bot = commands.Bot(command_prefix="!", test_guilds=[889176263992963142], intents=intents)
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), test_guilds=[889176263992963142])


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    for member in bot.get_all_members():
        print(member)


@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")


@bot.user_command()
async def avatar(inter, user):
    embed = disnake.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} is not cool")


@cool.command(name="bot")
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send("Yes, the bot is cool.")

@bot.command()
async def joined(ctx, member: disnake.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")


# Define a simple View that gives us a counter button
class Counter(disnake.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.primary)
    async def count(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = disnake.ButtonStyle.success
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)

    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def count2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = disnake.ButtonStyle.danger
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)
    
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def a(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def b(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def c(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def d(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def e(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def f(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def g(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def h(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def i(self):
        pass
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.secondary)
    async def j(self):
        pass


@bot.command()
async def counter(ctx: commands.Context):
    """Starts a counter for pressing."""
    await ctx.send("Press!", view=Counter())


TOKEN = open("TOKEN").readline()
bot.run(TOKEN)
