import nextcord
from nextcord.ui import *
from typing import *
from nextcord import SlashOption, InteractionMessage
from nextcord.ext import commands
from robotevents import *
from os import environ
import asyncio

token = ""

TESTING_GUILD_ID =   # Replace with your guild ID

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Show information on a team",)
async def team(
        interaction: nextcord.Interaction, team_choice: str = SlashOption(description="Team number", ),):
    my_team = find_team(team_choice)
    embed = nextcord.Embed(title=team_choice, url="https://www.robotevents.com/teams/VRC/" + team_choice)
    embed.add_field(name="Organization", value=my_team.get("organization"), inline=True)
    embed.add_field(name="Grade", value=my_team.get("grade"), inline=True)
    embed.add_field(name="Active", value=my_team.get("registered"), inline=True)

    view = View(timeout=None)
    select = nextcord.ui.StringSelect()
    select.add_option(label="Team Info", emoji="🗿", value="team")
    select.add_option(label="Awards", emoji="🏆", value="awards")
    select.add_option(label="Skills", emoji="📄", value="skills")
    select.add_option(label="Trueskill", emoji="📊", value="trueskill")
    select.add_option(label="Events", emoji="🗓️", value="events")

    async def select_callback(interaction):
        if select.values[0] == "team":
            embed.clear_fields()
            embed.add_field(name="Organization", value=my_team.get("organization"), inline=True)
            embed.add_field(name="Grade", value=my_team.get("grade"), inline=True)
            embed.add_field(name="Active", value=my_team.get("registered"), inline=True)
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "awards":
            embed.clear_fields()
            award_list = awards(my_team)
            for i in award_list:
                embed.add_field(name=i.get("title"), value=i.get("event").get("name"), inline=True)

            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "skills":
            embed.clear_fields()
            my_skills = global_skills(my_team)
            embed.add_field(name="World Skills Ranking", value=my_skills.get("rank"), inline=True)
            embed.add_field(name="Total Score", value=my_skills.get("scores").get("score"), inline=True)
            embed.add_field(name="Driver & Prog", value=str(my_skills.get("scores").get("driver")) + " & " + str(my_skills.get("scores").get("programming")), inline=True)
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "trueskill":
            embed.clear_fields()
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "events":
            embed.clear_fields()
            events_list = events(my_team)
            for i in events_list:
                embed.add_field(name=i.get("event").get("name"), value="\n", inline=False)
                embed.add_field(name="Division", value=i.get("division").get("name"), inline=True)
                embed.add_field(name="Ranking", value=i.get("rank"), inline=True)
                embed.add_field(name="Qualification Records", value=str(i.get("wins")) + "/" + str(i.get("losses")) + "/" + str(i.get("ties")), inline=True)
                embed.add_field(name="\n", value="\n", inline=False)
                embed.add_field(name="\n", value="\n", inline=False)

            await interaction.response.edit_message(embed=embed)

    select.callback = select_callback
    view.add_item(select)

    await interaction.send(embed=embed, view=view)

bot.run(token)
