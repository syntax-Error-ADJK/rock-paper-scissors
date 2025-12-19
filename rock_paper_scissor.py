import wx
import random
import pyttsx3
from cProfile import label
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import time
pygame.mixer.init()


my_list = ['scizzor', 'paper', 'rock']
turns=0
computer_score=0
player_score=0
draw=0
intro=0

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def music(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(base_dir, "sounds", filename)
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()



def on_start(event):
    title.Destroy()
    start_btn.Destroy()
    skip_introbtn.Hide()
    skipbtn=wx.Button(start_panel,label="Skip",pos=(380,450))
    skipbtn.Bind(wx.EVT_BUTTON,start_game)
    skipbtn.SetBackgroundColour("#bac095")
    intro1="Challenger, Welcome! 👋\n\nYou have stepped into the Arena of Three Powers — Rock, Paper, and Scissors.\nFor years, this arena has been guarded by the undefeated champion: Phantom Fist 👊🏾, \na super-intelligent bot built from millions of strategy simulations.\n\nPhantom Fist scans your moves, predicts your patterns, and adapts with\n lightning speed. ⚡\n But today… it faces YOU.\n\nWill you outsmart the machine?  \nWill intuition defeat calculation?  \nOnly one way to find out.\n\nChoose your move — Rock 🪨, Paper 📄, or Scissors ✂️ — and let the duel begin!"
    intro_voice = (
        "Challenger, Welcome! You have stepped into the Arena of Three Powers — Rock, Paper, and Scissors. "
        "For years, this arena has been guarded by the undefeated champion: Phantom Fist, a super-intelligent bot built from millions of strategy simulations. "
        "Phantom Fist scans your moves predicts your patterns and adapts with lightning speed. "
        "But today… it faces YOU. "
        "Will you outsmart the machine? Will intuition defeat calculation? Only one way to find out. "
        "Choose your move — Rock, Paper, or Scissors — and let the duel begin!"
    )
    intro = wx.StaticText(start_panel, label=intro1, pos=(25,160)) 
    intro.SetForegroundColour("#0a3b0c")
    speak(intro_voice)
    skipbtn.Hide()
    next_btn=wx.Button(start_panel, label="Next", pos=(328, 440),size=(160,30))
    next_btn.SetBackgroundColour("#bac095")
    next_btn.Bind(wx.EVT_BUTTON, start_game)

def start_game(event):
    global engine
    engine.stop()
    start_panel.Hide()
    panel1.Show()

def rules(event):
    wx.MessageBox("Winning rules:\n. Rock smashes scissors\n. Scissors cuts paper\n. Paper covers rock", "Rules")

def validate_turns(event):
    turns_value = turns_input.GetValue()
    if turns_value and int(turns_value) > 0:
        rockbtn.Enable()
        paperbtn.Enable()
        scizzorbtn.Enable()
    else:
        rockbtn.Disable()
        paperbtn.Disable()
        scizzorbtn.Disable()

def on_clickr(event):
    global turns, computer_score, player_score, draw
    player_name = name_input.GetValue() or "Player"
    turns_max = turns_input.GetValue()
    if turns < int(turns_max) and int(turns_max)>0:
        rand = random.choice(my_list)
        if rand == 'rock':
            a = "Aww, It was a tie :)"
            draw += 1
        elif rand == 'paper':
            a = "Phantom Fist won :("
            computer_score += 1
        else:
            a = "Congratulations you won!! :)"
            player_score += 1
        message = f"{player_name}'s Choice: Rock             Phantom Fist Choice: {rand}\n\n{a}"
        label.SetLabel(message)
        turns += 1
        name_input.Disable()
        turns_input.Disable()
    else:
        end_game(player_name)

def on_clickp(event):
    global turns, computer_score, player_score, draw
    player_name = name_input.GetValue() or "Player"
    turns_max = turns_input.GetValue()
    if turns < int(turns_max) and int(turns_max)>0:
        rand = random.choice(my_list)
        if rand == 'rock':
            a = "Congratulations you won!! :)"
            player_score += 1
        elif rand == 'paper':
            a = "Aww, It was a tie"
            draw += 1
        else:
            a = "Phantom Fist won :("
            computer_score += 1
        message = f"{player_name}'s Choice: Paper             Phantom Fist Choice: {rand}\n\n{a}"
        label.SetLabel(message)
        turns += 1
        name_input.Disable()
        turns_input.Disable()
    else:
        end_game(player_name)

def on_clicks(event):
    global turns, computer_score, player_score, draw
    player_name = name_input.GetValue() or "Player"
    turns_max = turns_input.GetValue()
    if turns < int(turns_max) and int(turns_max)>0:
        rand = random.choice(my_list)
        if rand == 'rock':
            a = "Phantom Fist won :("
            computer_score += 1
        elif rand == 'paper':
            a = "Congratulations you won!! :)"
            player_score += 1
        else:
            a = "Aww, It was tie"
            draw += 1
        message = f"{player_name}'s Choice: Scizzor             Phantom Fist Choice: {rand}\n\n{a}"
        label.SetLabel(message)
        turns += 1
        name_input.Disable()
        turns_input.Disable()
    else:
        end_game(player_name)

def end_game(player_name):
    global turns, computer_score, player_score, draw
    player_name = name_input.GetValue() or "Player"
    rockbtn.Disable()
    paperbtn.Disable()
    scizzorbtn.Disable()
    end_gamebtn.Disable()
    score = f"Game Over!\n\nFinal Scores:\n{player_name}: {player_score}\nComputer: {computer_score}\nDraws: {draw}"
    Score.SetLabel(score)
    play_againbtn = wx.Button(panel1, label="Play Again", pos=(200, 520))
    play_againbtn.SetBackgroundColour("#ffd3ac")
    exitbtn = wx.Button(panel1, label="Exit", pos=(320, 520))
    exitbtn.SetBackgroundColour("#ffd3ac")
    play_againbtn.Bind(wx.EVT_BUTTON, on_play_again)
    play_againbtn.SetBackgroundColour("#bac095")
    exitbtn.Bind(wx.EVT_BUTTON, on_exit)
    exitbtn.SetBackgroundColour("#bac095")

    if player_score == computer_score:
        music("lost-the-game-effect-230571.mp3")
        wx.MessageBox("It was a Tie", " ")
    elif player_score > computer_score:
        music("victorymale-version-230553.mp3")
        wx.MessageBox("Glory is yours, brave warrior!", " ")
    else:
        music("lost-the-game-effect-230571.mp3")
        wx.MessageBox("Better luck next time Challenger", " ")


def on_play_again(event):
    global turns, computer_score, player_score, draw
    turns = 0
    computer_score = 0
    player_score = 0
    draw = 0
    start_panel.Hide()
    panel1.Show()
    label.SetLabel("Start playing")
    Score.SetLabel("")
    turns_input.Enable()

    end_gamebtn.Enable()

def on_exit(event):
    frame.Close()

app = wx.App()
frame = wx.Frame(None, title="Rock Paper Scizzor Game", size=(519, 642))

start_panel = wx.Panel(frame, size=(500,600), pos=(0,0))
start_panel.SetBackgroundColour("#cfda8d")
title = wx.StaticText(start_panel, label="Rock Paper Scizzor", pos=(120,180))
title.SetFont(wx.Font(22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
title.SetForegroundColour("#0a3b0c")
start_btn = wx.Button(start_panel, label="Start Game", pos=(190,260), size=(120,40))
start_btn.SetBackgroundColour("#bac095")
start_btn.Bind(wx.EVT_BUTTON, on_start)
skip_introbtn= wx.Button(start_panel, label="Skip Intro", pos=(210,310))
skip_introbtn.Bind(wx.EVT_BUTTON, on_play_again)
skip_introbtn.SetBackgroundColour("#bac095")
rules_btn = wx.Button(start_panel, label="Rules", pos=(380,500))
rules_btn.SetBackgroundColour("#bac095")
rules_btn.Bind(wx.EVT_BUTTON, rules)

panel1 = wx.Panel(frame, size=(500, 600))
panel1.SetBackgroundColour("#d4de95")

panel2 = wx.Panel(frame, size=(500, 13), pos=(0, 0))
panel2.SetBackgroundColour("#636b2f")

panel3 = wx.Panel(frame, size=(500, 13), pos=(0, 590))
panel3.SetBackgroundColour("#636b2f")

panel4 = wx.Panel(frame, size=(13, 600), pos=(0, 0))
panel4.SetBackgroundColour("#636b2f")   

panel5 = wx.Panel(frame, size=(13, 600), pos=(490, 0))
panel5.SetBackgroundColour("#636b2f")

panel1.Hide()

name_label = wx.StaticText(panel1, label="Enter Your Name:", pos=(50, 30))
name_input = wx.TextCtrl(panel1, pos=(50, 60), size=(200, 25))
name_input.SetBackgroundColour("#bac095")

turns_label = wx.StaticText(panel1, label="Enter Number of Turns:", pos=(50, 100))
turns_input = wx.TextCtrl(panel1, pos=(50, 130), size=(200, 25))
turns_input.SetBackgroundColour("#bac095")
turns_input.Bind(wx.EVT_TEXT, validate_turns)

rockbtn = wx.Button(panel1, label="Rock 👊🏽", pos=(50, 190),size=(100,30))
rockbtn.SetBackgroundColour("#755E34C1")
rockbtn.Disable()
paperbtn = wx.Button(panel1, label="Paper ✋🏽", pos=(200, 190),size=(100,30))
paperbtn.SetBackgroundColour("#dadfbc")
paperbtn.Disable()
scizzorbtn = wx.Button(panel1, label="Scissor ✌🏽", pos=(350, 190),size=(100,30))
scizzorbtn.SetBackgroundColour("#8491ac")
scizzorbtn.Disable()
seperator = wx.StaticText(panel1, label="---------------------------------------------------------------------------------------------", pos=(14, 250))

label = wx.StaticText(panel1, label="Start playing", pos=(50, 280))

seperator = wx.StaticText(panel1, label="---------------------------------------------------------------------------------------------", pos=(14, 350))
rockbtn.Bind(wx.EVT_BUTTON, on_clickr)
paperbtn.Bind(wx.EVT_BUTTON, on_clickp)
scizzorbtn.Bind(wx.EVT_BUTTON, on_clicks)

Scorei = wx.StaticText(panel1, label="                                              S C O R E   B O A R D \n                                             -----------------------", pos=(50, 370))
Score = wx.StaticText(panel1, label="", pos=(50, 400))
end_gamebtn = wx.Button(panel1, label="End Game", pos=(80, 520))   
end_gamebtn.SetBackgroundColour("#ffd3ac")
end_gamebtn.Bind(wx.EVT_BUTTON, end_game)
frame.Show()

app.MainLoop()
