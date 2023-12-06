import nextcord
from nextcord.ui import *
from typing import *
from nextcord import SlashOption, InteractionMessage
from nextcord.ext import commands
from robotevents import *
from vrcdataanalysis import *
from os import environ
import asyncio

token = environ["TOKEN"]

TESTING_GUILD_ID = int # Replace with your guild ID

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Show information on a team",)
async def team(
        interaction: nextcord.Interaction, team_choice: str = SlashOption(description="Team number", ),):
    request_url = 'https://www.robotevents.com/api/v2/teams?number%5B%5D='+ team + '&program%5B%5D=1&myTeams=false'
    r = requests.get(request_url, headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNDRiMmZmZTlkZGZlZTg1N2VjNGY3MWI2Y2I5OTkyZjNjYzIzYTI4NzdmMTY5NGExMzUzNWJlZTBjY2I2NGI5YTVjMWQ4MjlmMmFjZTcxNjEiLCJpYXQiOjE3MDE3MjMwMDUuNzc2MDk0LCJuYmYiOjE3MDE3MjMwMDUuNzc2MDk3MSwiZXhwIjoyNjQ4NDk0MjA1Ljc2NjEyNTIsInN1YiI6IjExMzQ4NiIsInNjb3BlcyI6W119.iUofrpTGHmKIUvOw2CcG5E9yDgDl6ZNT7UGDkS49q1dEhutfmQQiR8Eic4_iCxP74ZHqoRCmsu0L5LDzyrgJ2Jbv6p7XnSvjQlFsS32FGH_5s2bhkXAmnp_PU7ElqIlJ-zda5xV7OR3UWZz_GrE_6PGWjtTPWaeAwckBWYVCLQM7dVmlDKofEmv28fea3Y711UxD7Y1c3adZP9Ja47esw2sQ8Ae1OtUoPZ-wfkiMiApTzSovUJ27SJEuldD7TZMKFVEKkXz39PHeDVLk6mnFKn4Xc20Y2rHsAgoRSZgC5A9f8uDkUqVmM8L0kRkS7NuOX0A7bqO8H6f5CiaZhNON6VRi2FzIvddYQub45xfdVC6BhjaI_OBd7cWNe4jebWYIs9aOYni119B0FN4DAhqImA-I0TbGvDvxFLMmOzIty8wNFSGOmZzymIXKc1m4_T6TaOhVWBZv4sDo5ABIVUJuXP1juR53iyiU5QHRaZRYlRSWh6JImfCOZF4OjBbTsNtORaZB7Sarv3tjNNCMCpwD4GrjK6ZitxawKVArz5WDr6lEBXhiRpuViatn1xGJo-X2coAJzHBew7rUJUuk5bqRhurOJiE2sPm46hlghArbiHp96J3wHPgKG7TVF6NfgLIoyw2UjbmcakaRDF-6mNwctauNnLo98B7glJ4QMwvb_5U'})
    print(r)
    # API_Data = r.json()
    # return API_Data["data"][0]
    # my_team = find_team(team_choice)
    # embed = nextcord.Embed(title=team_choice, url="https://www.robotevents.com/teams/VRC/" + team_choice + " " + my_team.get("team_name"))
    # embed.add_field(name="Organization", value=my_team.get("organization"), inline=True)
    # embed.add_field(name="Grade", value=my_team.get("grade"), inline=True)
    # embed.add_field(name="Active", value=my_team.get("registered"), inline=True)
    # embed.add_field(name="Location", value=location_data(my_team).get("city") + ", " + location_data(my_team).get("region") + ", " + location_data(my_team).get("country"), inline=False)


    # view = View(timeout=None)
    # select = nextcord.ui.StringSelect()
    # select.add_option(label="Team Info", emoji="🪪", value="team")
    # select.add_option(label="Awards", emoji="🏆", value="awards")
    # select.add_option(label="Skills", emoji="📄", value="skills")
    # #select.add_option(label="Trueskill", emoji="📊", value="trueskill")
    # select.add_option(label="Events", emoji="🗓️", value="events")

    # async def select_callback(interaction):
    #     if select.values[0] == "team":
    #         embed.clear_fields()
    #         embed.add_field(name="Organization", value=my_team.get("organization"), inline=True)
    #         embed.add_field(name="Grade", value=my_team.get("grade"), inline=True)
    #         embed.add_field(name="Active", value=my_team.get("registered"), inline=True)
    #         embed.add_field(name="Location", value=location_data(my_team).get("city") + ", " + location_data(my_team).get("region") + ", " + location_data(my_team).get("country"))
    #         await interaction.response.edit_message(embed=embed)

    #     elif select.values[0] == "awards":
    #         embed.clear_fields()
    #         award_list = awards(my_team)
    #         for i in award_list:
    #             embed.add_field(name=i.get("title"), value=i.get("event").get("name"), inline=True)

    #         await interaction.response.edit_message(embed=embed)

    #     elif select.values[0] == "skills":
    #         embed.clear_fields()
    #         my_skills = global_skills(my_team)
    #         embed.add_field(name="World Skills Ranking", value=my_skills.get("rank"), inline=True)
    #         embed.add_field(name="Total Score", value=my_skills.get("scores").get("score"), inline=True)
    #         embed.add_field(name="Driver & Prog", value=str(my_skills.get("scores").get("driver")) + " & " + str(my_skills.get("scores").get("programming")), inline=True)
    #         await interaction.response.edit_message(embed=embed)

    #     elif select.values[0] == "trueskill":
    #         embed.clear_fields()
    #         #embed.add_field(name="Trueskill Ranking", value=team_trueskill_ranking(team_choice), inline=True)
    #         #embed.add_field(name="Trueskill Value", value=team_trueskill_value(team_choice), inline=True)
    #         await interaction.response.edit_message(embed=embed)

    #     elif select.values[0] == "events":
    #         embed.clear_fields()
    #         events_list = events(my_team)
    #         for i in events_list:
    #             embed.add_field(name=i.get("event").get("name"), value="\n", inline=False)
    #             embed.add_field(name="Division", value=i.get("division").get("name"), inline=True)
    #             embed.add_field(name="Ranking", value=i.get("rank"), inline=True)
    #             embed.add_field(name="Qualification Records", value=str(i.get("wins")) + "/" + str(i.get("losses")) + "/" + str(i.get("ties")), inline=True)
    #             embed.add_field(name="\n", value="\n", inline=False)
    #             embed.add_field(name="\n", value="\n", inline=False)

    #         await interaction.response.edit_message(embed=embed)

    select.callback = select_callback
    view.add_item(select)

    await interaction.send(embed=embed, view=view)

@bot.slash_command(description="Get trueskill match prediction",)
async def predict(
        interaction: nextcord.Interaction,
        red1: str = SlashOption(description="Team number", ),
        red2: str = SlashOption(description="Team number", ),
        blue1: str = SlashOption(description="Team number", ),
        blue2: str = SlashOption(description="Team number", ),):
        pred = prediction(red1, red2, blue1, blue2)
        embed = nextcord.Embed(title="{} {} vs {} {}".format(red1 ,red2, blue1, blue2))
        embed.add_field(name="Prediction", value=pred.get("prediction_msg"), inline=True)
        await interaction.send(embed=embed)

bot.run(token)
