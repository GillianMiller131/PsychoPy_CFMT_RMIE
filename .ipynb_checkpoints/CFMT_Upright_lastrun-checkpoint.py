#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on Sat May  4 17:15:44 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.3'
expName = 'CFMT_Upright'  # from the Builder filename that created this script
expInfo = {
    'participant': 'P0',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data_raw/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/gillian/Documents/GitHub/PsychoPy_CFMT_RMIE/CFMT_Upright_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions_Task" ---
text = visual.TextStim(win=win, name='text',
    text='In the following task you will be required to memorize the faces of different individuals. \n\nYou will then be asked to identify a face you memorized out of a line-up of three faces. \n\nThe test will begin with a very easy practice round and then will become progressively more challenging. \n\nInstructions will be given throughout the task, please follow them carefully. \n\nThe test will take approximately 15 minutes to complete. \n\n[]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_Practice" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Practice\n\nMemorize the face in the next three images.\n\nA test will follow.\n\n[]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Practice_Memorize" ---
prac_mem_1 = visual.ImageStim(
    win=win,
    name='prac_mem_1', 
    image='CFMT/Practice/1.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
prac_mem_2 = visual.ImageStim(
    win=win,
    name='prac_mem_2', 
    image='CFMT/Practice/2.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_mem_3 = visual.ImageStim(
    win=win,
    name='prac_mem_3', 
    image='CFMT/Practice/3.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_title = visual.TextStim(win=win, name='prac_title',
    text='Practice',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Practice_Response" ---
Practice_Prompt = visual.TextStim(win=win, name='Practice_Prompt',
    text='What face did you see?\n\nThere is only one correct answer. ',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Practice_Choices = visual.ImageStim(
    win=win,
    name='Practice_Choices', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers = visual.ImageStim(
    win=win,
    name='Numbers', units='norm', 
    image='CFMT/ans_num.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Response = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_part1" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text="Great! Let's go on and do the actual test.\n\nIn this test you will learn to recognize six people. \n\n[]",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_prompt_part1" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='Try and memorize the following face.\n\nReady?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Memorize_part1" ---
mem_1 = visual.ImageStim(
    win=win,
    name='mem_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.28, 0.308),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mem_2 = visual.ImageStim(
    win=win,
    name='mem_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.28, 0.308),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mem_3 = visual.ImageStim(
    win=win,
    name='mem_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.28, 0.308),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mem_title = visual.TextStim(win=win, name='mem_title',
    text='Memorize',
    font='Open Sans',
    units='norm', pos=(0, 0.45), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Test1" ---
Answer_Prompt = visual.TextStim(win=win, name='Answer_Prompt',
    text='What face did you just see?\n\n',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choices = visual.ImageStim(
    win=win,
    name='Choices', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers_Test1 = visual.ImageStim(
    win=win,
    name='Numbers_Test1', units='norm', 
    image='CFMT/ans_num.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Answer = keyboard.Keyboard()
fnum_1 = visual.TextStim(win=win, name='fnum_1',
    text='',
    font='Open Sans',
    units='norm', pos=(0.8, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Test2" ---
Answer_Prompt_2 = visual.TextStim(win=win, name='Answer_Prompt_2',
    text='What face did you just see?\n\n',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choices_2 = visual.ImageStim(
    win=win,
    name='Choices_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers_Test1_2 = visual.ImageStim(
    win=win,
    name='Numbers_Test1_2', units='norm', 
    image='CFMT/ans_num.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Answer_2 = keyboard.Keyboard()
fnum_2 = visual.TextStim(win=win, name='fnum_2',
    text='',
    font='Open Sans',
    units='norm', pos=(0.8, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Test3" ---
Answer_Prompt_3 = visual.TextStim(win=win, name='Answer_Prompt_3',
    text='What face did you just see?\n\n',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choices_3 = visual.ImageStim(
    win=win,
    name='Choices_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers_Test3 = visual.ImageStim(
    win=win,
    name='Numbers_Test3', units='norm', 
    image='CFMT/ans_num.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Answer_3 = keyboard.Keyboard()
fnum_3 = visual.TextStim(win=win, name='fnum_3',
    text='',
    font='Open Sans',
    units='norm', pos=(0.8, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Instructions_test" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='Now you will review the same 6 people for 20 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
array_1 = visual.ImageStim(
    win=win,
    name='array_1', 
    image='CFMT/Test/array.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Now your memory of those face will be tested. \n\nIn the remaining trials, the correct answer can be any of the six faces.\n\nThe incorrect faces are sometimes very similar to the target faces, so be sure to look at each face prior to answering. \n\n[]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Part2_novel" ---
Answer_Prompt_4 = visual.TextStim(win=win, name='Answer_Prompt_4',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choices_4 = visual.ImageStim(
    win=win,
    name='Choices_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers_Test3_2 = visual.ImageStim(
    win=win,
    name='Numbers_Test3_2', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Answer_4 = keyboard.Keyboard()
novnum = visual.TextStim(win=win, name='novnum',
    text='',
    font='Open Sans',
    units='norm', pos=(0.8, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "instructions_part2_noise" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='Now you will review the same 6 people for 20 seconds. \n\nThen your memory of those faces will be tested.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='CFMT/Test/array.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Part2_noise" ---
Answer_Prompt_5 = visual.TextStim(win=win, name='Answer_Prompt_5',
    text='Which face is one of the six target faces?\n\n\n',
    font='Open Sans',
    units='norm', pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Choices_5 = visual.ImageStim(
    win=win,
    name='Choices_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Numbers_Test3_3 = visual.ImageStim(
    win=win,
    name='Numbers_Test3_3', units='norm', 
    image='CFMT/ans_num.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(1.046, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Answer_5 = keyboard.Keyboard()
noisnum = visual.TextStim(win=win, name='noisnum',
    text='',
    font='Open Sans',
    units='norm', pos=(0.8, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "End" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='Great Work!\n\n[]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions_Task" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Instructions_TaskComponents = [text, key_resp]
for thisComponent in Instructions_TaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_Task" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_TaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_Task" ---
for thisComponent in Instructions_TaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions_Task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_Practice" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instructions_PracticeComponents = [text_2, key_resp_2]
for thisComponent in Instructions_PracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_Practice" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_PracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_Practice" ---
for thisComponent in Instructions_PracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions_Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Practice_Memorize" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_MemorizeComponents = [prac_mem_1, prac_mem_2, prac_mem_3, prac_title]
for thisComponent in Practice_MemorizeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_Memorize" ---
while continueRoutine and routineTimer.getTime() < 9.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_mem_1* updates
    if prac_mem_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_mem_1.frameNStart = frameN  # exact frame index
        prac_mem_1.tStart = t  # local t and not account for scr refresh
        prac_mem_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_mem_1, 'tStartRefresh')  # time at next scr refresh
        prac_mem_1.setAutoDraw(True)
    if prac_mem_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prac_mem_1.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            prac_mem_1.tStop = t  # not accounting for scr refresh
            prac_mem_1.frameNStop = frameN  # exact frame index
            prac_mem_1.setAutoDraw(False)
    
    # *prac_mem_2* updates
    if prac_mem_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        prac_mem_2.frameNStart = frameN  # exact frame index
        prac_mem_2.tStart = t  # local t and not account for scr refresh
        prac_mem_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_mem_2, 'tStartRefresh')  # time at next scr refresh
        prac_mem_2.setAutoDraw(True)
    if prac_mem_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prac_mem_2.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            prac_mem_2.tStop = t  # not accounting for scr refresh
            prac_mem_2.frameNStop = frameN  # exact frame index
            prac_mem_2.setAutoDraw(False)
    
    # *prac_mem_3* updates
    if prac_mem_3.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
        # keep track of start time/frame for later
        prac_mem_3.frameNStart = frameN  # exact frame index
        prac_mem_3.tStart = t  # local t and not account for scr refresh
        prac_mem_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_mem_3, 'tStartRefresh')  # time at next scr refresh
        prac_mem_3.setAutoDraw(True)
    if prac_mem_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prac_mem_3.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            prac_mem_3.tStop = t  # not accounting for scr refresh
            prac_mem_3.frameNStop = frameN  # exact frame index
            prac_mem_3.setAutoDraw(False)
    
    # *prac_title* updates
    if prac_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_title.frameNStart = frameN  # exact frame index
        prac_title.tStart = t  # local t and not account for scr refresh
        prac_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_title, 'tStartRefresh')  # time at next scr refresh
        prac_title.setAutoDraw(True)
    if prac_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prac_title.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            prac_title.tStop = t  # not accounting for scr refresh
            prac_title.frameNStop = frameN  # exact frame index
            prac_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_MemorizeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_Memorize" ---
for thisComponent in Practice_MemorizeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-9.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CFMT/Practice.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Practice_Response" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Practice_Choices.setImage(prac)
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    Practice_ResponseComponents = [Practice_Prompt, Practice_Choices, Numbers, Response]
    for thisComponent in Practice_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Practice_Response" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Practice_Prompt* updates
        if Practice_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Practice_Prompt.frameNStart = frameN  # exact frame index
            Practice_Prompt.tStart = t  # local t and not account for scr refresh
            Practice_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Practice_Prompt, 'tStartRefresh')  # time at next scr refresh
            Practice_Prompt.setAutoDraw(True)
        
        # *Practice_Choices* updates
        if Practice_Choices.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Practice_Choices.frameNStart = frameN  # exact frame index
            Practice_Choices.tStart = t  # local t and not account for scr refresh
            Practice_Choices.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Practice_Choices, 'tStartRefresh')  # time at next scr refresh
            Practice_Choices.setAutoDraw(True)
        
        # *Numbers* updates
        if Numbers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers.frameNStart = frameN  # exact frame index
            Numbers.tStart = t  # local t and not account for scr refresh
            Numbers.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers, 'tStartRefresh')  # time at next scr refresh
            Numbers.setAutoDraw(True)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Practice_Response" ---
    for thisComponent in Practice_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
    trials.addData('Response.keys',Response.keys)
    if Response.keys != None:  # we had a response
        trials.addData('Response.rt', Response.rt)
    # the Routine "Practice_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "Instructions_part1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions_part1Components = [text_3, key_resp_3]
for thisComponent in Instructions_part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_part1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_part1" ---
for thisComponent in Instructions_part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions_part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Part1_Learn = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CFMT/Learn.xlsx'),
    seed=None, name='Part1_Learn')
thisExp.addLoop(Part1_Learn)  # add the loop to the experiment
thisPart1_Learn = Part1_Learn.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPart1_Learn.rgb)
if thisPart1_Learn != None:
    for paramName in thisPart1_Learn:
        exec('{} = thisPart1_Learn[paramName]'.format(paramName))

for thisPart1_Learn in Part1_Learn:
    currentLoop = Part1_Learn
    # abbreviate parameter names if possible (e.g. rgb = thisPart1_Learn.rgb)
    if thisPart1_Learn != None:
        for paramName in thisPart1_Learn:
            exec('{} = thisPart1_Learn[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Instructions_prompt_part1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Instructions_prompt_part1Components = [text_4]
    for thisComponent in Instructions_prompt_part1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_prompt_part1" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_prompt_part1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_prompt_part1" ---
    for thisComponent in Instructions_prompt_part1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Memorize_part1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    mem_1.setImage(Mem1)
    mem_2.setImage(Mem2)
    mem_3.setImage(Mem3)
    # keep track of which components have finished
    Memorize_part1Components = [mem_1, mem_2, mem_3, mem_title]
    for thisComponent in Memorize_part1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Memorize_part1" ---
    while continueRoutine and routineTimer.getTime() < 9.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mem_1* updates
        if mem_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mem_1.frameNStart = frameN  # exact frame index
            mem_1.tStart = t  # local t and not account for scr refresh
            mem_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mem_1, 'tStartRefresh')  # time at next scr refresh
            mem_1.setAutoDraw(True)
        if mem_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mem_1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                mem_1.tStop = t  # not accounting for scr refresh
                mem_1.frameNStop = frameN  # exact frame index
                mem_1.setAutoDraw(False)
        
        # *mem_2* updates
        if mem_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            mem_2.frameNStart = frameN  # exact frame index
            mem_2.tStart = t  # local t and not account for scr refresh
            mem_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mem_2, 'tStartRefresh')  # time at next scr refresh
            mem_2.setAutoDraw(True)
        if mem_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mem_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                mem_2.tStop = t  # not accounting for scr refresh
                mem_2.frameNStop = frameN  # exact frame index
                mem_2.setAutoDraw(False)
        
        # *mem_3* updates
        if mem_3.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            mem_3.frameNStart = frameN  # exact frame index
            mem_3.tStart = t  # local t and not account for scr refresh
            mem_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mem_3, 'tStartRefresh')  # time at next scr refresh
            mem_3.setAutoDraw(True)
        if mem_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mem_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                mem_3.tStop = t  # not accounting for scr refresh
                mem_3.frameNStop = frameN  # exact frame index
                mem_3.setAutoDraw(False)
        
        # *mem_title* updates
        if mem_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mem_title.frameNStart = frameN  # exact frame index
            mem_title.tStart = t  # local t and not account for scr refresh
            mem_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mem_title, 'tStartRefresh')  # time at next scr refresh
            mem_title.setAutoDraw(True)
        if mem_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mem_title.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                mem_title.tStop = t  # not accounting for scr refresh
                mem_title.frameNStop = frameN  # exact frame index
                mem_title.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Memorize_part1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Memorize_part1" ---
    for thisComponent in Memorize_part1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-9.000000)
    
    # --- Prepare to start Routine "Test1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Choices.setImage(Test1)
    Answer.keys = []
    Answer.rt = []
    _Answer_allKeys = []
    fnum_1.setText(facenum)
    # keep track of which components have finished
    Test1Components = [Answer_Prompt, Choices, Numbers_Test1, Answer, fnum_1]
    for thisComponent in Test1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answer_Prompt* updates
        if Answer_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_Prompt.frameNStart = frameN  # exact frame index
            Answer_Prompt.tStart = t  # local t and not account for scr refresh
            Answer_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_Prompt, 'tStartRefresh')  # time at next scr refresh
            Answer_Prompt.setAutoDraw(True)
        
        # *Choices* updates
        if Choices.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choices.frameNStart = frameN  # exact frame index
            Choices.tStart = t  # local t and not account for scr refresh
            Choices.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choices, 'tStartRefresh')  # time at next scr refresh
            Choices.setAutoDraw(True)
        
        # *Numbers_Test1* updates
        if Numbers_Test1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers_Test1.frameNStart = frameN  # exact frame index
            Numbers_Test1.tStart = t  # local t and not account for scr refresh
            Numbers_Test1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers_Test1, 'tStartRefresh')  # time at next scr refresh
            Numbers_Test1.setAutoDraw(True)
        
        # *Answer* updates
        waitOnFlip = False
        if Answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer.frameNStart = frameN  # exact frame index
            Answer.tStart = t  # local t and not account for scr refresh
            Answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer, 'tStartRefresh')  # time at next scr refresh
            Answer.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Answer.status == STARTED and not waitOnFlip:
            theseKeys = Answer.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Answer_allKeys.extend(theseKeys)
            if len(_Answer_allKeys):
                Answer.keys = _Answer_allKeys[-1].name  # just the last key pressed
                Answer.rt = _Answer_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fnum_1* updates
        if fnum_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fnum_1.frameNStart = frameN  # exact frame index
            fnum_1.tStart = t  # local t and not account for scr refresh
            fnum_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fnum_1, 'tStartRefresh')  # time at next scr refresh
            fnum_1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test1" ---
    for thisComponent in Test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer.keys in ['', [], None]:  # No response was made
        Answer.keys = None
    Part1_Learn.addData('Answer.keys',Answer.keys)
    if Answer.keys != None:  # we had a response
        Part1_Learn.addData('Answer.rt', Answer.rt)
    # the Routine "Test1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Test2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Choices_2.setImage(Test2)
    Answer_2.keys = []
    Answer_2.rt = []
    _Answer_2_allKeys = []
    fnum_2.setText(facenum)
    # keep track of which components have finished
    Test2Components = [Answer_Prompt_2, Choices_2, Numbers_Test1_2, Answer_2, fnum_2]
    for thisComponent in Test2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answer_Prompt_2* updates
        if Answer_Prompt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_Prompt_2.frameNStart = frameN  # exact frame index
            Answer_Prompt_2.tStart = t  # local t and not account for scr refresh
            Answer_Prompt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_Prompt_2, 'tStartRefresh')  # time at next scr refresh
            Answer_Prompt_2.setAutoDraw(True)
        
        # *Choices_2* updates
        if Choices_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choices_2.frameNStart = frameN  # exact frame index
            Choices_2.tStart = t  # local t and not account for scr refresh
            Choices_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choices_2, 'tStartRefresh')  # time at next scr refresh
            Choices_2.setAutoDraw(True)
        
        # *Numbers_Test1_2* updates
        if Numbers_Test1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers_Test1_2.frameNStart = frameN  # exact frame index
            Numbers_Test1_2.tStart = t  # local t and not account for scr refresh
            Numbers_Test1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers_Test1_2, 'tStartRefresh')  # time at next scr refresh
            Numbers_Test1_2.setAutoDraw(True)
        
        # *Answer_2* updates
        waitOnFlip = False
        if Answer_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_2.frameNStart = frameN  # exact frame index
            Answer_2.tStart = t  # local t and not account for scr refresh
            Answer_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_2, 'tStartRefresh')  # time at next scr refresh
            Answer_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Answer_2.status == STARTED and not waitOnFlip:
            theseKeys = Answer_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Answer_2_allKeys.extend(theseKeys)
            if len(_Answer_2_allKeys):
                Answer_2.keys = _Answer_2_allKeys[-1].name  # just the last key pressed
                Answer_2.rt = _Answer_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fnum_2* updates
        if fnum_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fnum_2.frameNStart = frameN  # exact frame index
            fnum_2.tStart = t  # local t and not account for scr refresh
            fnum_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fnum_2, 'tStartRefresh')  # time at next scr refresh
            fnum_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test2" ---
    for thisComponent in Test2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer_2.keys in ['', [], None]:  # No response was made
        Answer_2.keys = None
    Part1_Learn.addData('Answer_2.keys',Answer_2.keys)
    if Answer_2.keys != None:  # we had a response
        Part1_Learn.addData('Answer_2.rt', Answer_2.rt)
    # the Routine "Test2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Test3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Choices_3.setImage(Test3)
    Answer_3.keys = []
    Answer_3.rt = []
    _Answer_3_allKeys = []
    fnum_3.setText(facenum)
    # keep track of which components have finished
    Test3Components = [Answer_Prompt_3, Choices_3, Numbers_Test3, Answer_3, fnum_3]
    for thisComponent in Test3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answer_Prompt_3* updates
        if Answer_Prompt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_Prompt_3.frameNStart = frameN  # exact frame index
            Answer_Prompt_3.tStart = t  # local t and not account for scr refresh
            Answer_Prompt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_Prompt_3, 'tStartRefresh')  # time at next scr refresh
            Answer_Prompt_3.setAutoDraw(True)
        
        # *Choices_3* updates
        if Choices_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choices_3.frameNStart = frameN  # exact frame index
            Choices_3.tStart = t  # local t and not account for scr refresh
            Choices_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choices_3, 'tStartRefresh')  # time at next scr refresh
            Choices_3.setAutoDraw(True)
        
        # *Numbers_Test3* updates
        if Numbers_Test3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers_Test3.frameNStart = frameN  # exact frame index
            Numbers_Test3.tStart = t  # local t and not account for scr refresh
            Numbers_Test3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers_Test3, 'tStartRefresh')  # time at next scr refresh
            Numbers_Test3.setAutoDraw(True)
        
        # *Answer_3* updates
        waitOnFlip = False
        if Answer_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_3.frameNStart = frameN  # exact frame index
            Answer_3.tStart = t  # local t and not account for scr refresh
            Answer_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_3, 'tStartRefresh')  # time at next scr refresh
            Answer_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Answer_3.status == STARTED and not waitOnFlip:
            theseKeys = Answer_3.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Answer_3_allKeys.extend(theseKeys)
            if len(_Answer_3_allKeys):
                Answer_3.keys = _Answer_3_allKeys[-1].name  # just the last key pressed
                Answer_3.rt = _Answer_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fnum_3* updates
        if fnum_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fnum_3.frameNStart = frameN  # exact frame index
            fnum_3.tStart = t  # local t and not account for scr refresh
            fnum_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fnum_3, 'tStartRefresh')  # time at next scr refresh
            fnum_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test3" ---
    for thisComponent in Test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer_3.keys in ['', [], None]:  # No response was made
        Answer_3.keys = None
    Part1_Learn.addData('Answer_3.keys',Answer_3.keys)
    if Answer_3.keys != None:  # we had a response
        Part1_Learn.addData('Answer_3.rt', Answer_3.rt)
    # the Routine "Test3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Part1_Learn'


# --- Prepare to start Routine "Instructions_test" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Instructions_testComponents = [text_5, array_1, text_6, key_resp_4]
for thisComponent in Instructions_testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_test" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            text_5.setAutoDraw(False)
    
    # *array_1* updates
    if array_1.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        array_1.frameNStart = frameN  # exact frame index
        array_1.tStart = t  # local t and not account for scr refresh
        array_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_1, 'tStartRefresh')  # time at next scr refresh
        array_1.setAutoDraw(True)
    if array_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_1.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            array_1.tStop = t  # not accounting for scr refresh
            array_1.frameNStop = frameN  # exact frame index
            array_1.setAutoDraw(False)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 24.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_4* updates
    if key_resp_4.status == NOT_STARTED and t >= 24.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_test" ---
for thisComponent in Instructions_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
novel_test = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CFMT/Test_novel.xlsx'),
    seed=None, name='novel_test')
thisExp.addLoop(novel_test)  # add the loop to the experiment
thisNovel_test = novel_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNovel_test.rgb)
if thisNovel_test != None:
    for paramName in thisNovel_test:
        exec('{} = thisNovel_test[paramName]'.format(paramName))

for thisNovel_test in novel_test:
    currentLoop = novel_test
    # abbreviate parameter names if possible (e.g. rgb = thisNovel_test.rgb)
    if thisNovel_test != None:
        for paramName in thisNovel_test:
            exec('{} = thisNovel_test[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Part2_novel" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Answer_Prompt_4.setText('Which face is one of the six target faces?\n\n\n')
    Choices_4.setImage(novel)
    Numbers_Test3_2.setImage('CFMT/ans_num.png')
    Answer_4.keys = []
    Answer_4.rt = []
    _Answer_4_allKeys = []
    novnum.setText(nov_num)
    # keep track of which components have finished
    Part2_novelComponents = [Answer_Prompt_4, Choices_4, Numbers_Test3_2, Answer_4, novnum]
    for thisComponent in Part2_novelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Part2_novel" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answer_Prompt_4* updates
        if Answer_Prompt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_Prompt_4.frameNStart = frameN  # exact frame index
            Answer_Prompt_4.tStart = t  # local t and not account for scr refresh
            Answer_Prompt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_Prompt_4, 'tStartRefresh')  # time at next scr refresh
            Answer_Prompt_4.setAutoDraw(True)
        
        # *Choices_4* updates
        if Choices_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choices_4.frameNStart = frameN  # exact frame index
            Choices_4.tStart = t  # local t and not account for scr refresh
            Choices_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choices_4, 'tStartRefresh')  # time at next scr refresh
            Choices_4.setAutoDraw(True)
        
        # *Numbers_Test3_2* updates
        if Numbers_Test3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers_Test3_2.frameNStart = frameN  # exact frame index
            Numbers_Test3_2.tStart = t  # local t and not account for scr refresh
            Numbers_Test3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers_Test3_2, 'tStartRefresh')  # time at next scr refresh
            Numbers_Test3_2.setAutoDraw(True)
        
        # *Answer_4* updates
        waitOnFlip = False
        if Answer_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_4.frameNStart = frameN  # exact frame index
            Answer_4.tStart = t  # local t and not account for scr refresh
            Answer_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_4, 'tStartRefresh')  # time at next scr refresh
            Answer_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Answer_4.status == STARTED and not waitOnFlip:
            theseKeys = Answer_4.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Answer_4_allKeys.extend(theseKeys)
            if len(_Answer_4_allKeys):
                Answer_4.keys = _Answer_4_allKeys[-1].name  # just the last key pressed
                Answer_4.rt = _Answer_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *novnum* updates
        if novnum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            novnum.frameNStart = frameN  # exact frame index
            novnum.tStart = t  # local t and not account for scr refresh
            novnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(novnum, 'tStartRefresh')  # time at next scr refresh
            novnum.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part2_novelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Part2_novel" ---
    for thisComponent in Part2_novelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer_4.keys in ['', [], None]:  # No response was made
        Answer_4.keys = None
    novel_test.addData('Answer_4.keys',Answer_4.keys)
    if Answer_4.keys != None:  # we had a response
        novel_test.addData('Answer_4.rt', Answer_4.rt)
    # the Routine "Part2_novel" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'novel_test'


# --- Prepare to start Routine "instructions_part2_noise" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
instructions_part2_noiseComponents = [text_7, image]
for thisComponent in instructions_part2_noiseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_part2_noise" ---
while continueRoutine and routineTimer.getTime() < 24.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            text_7.setAutoDraw(False)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.stopped')
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_part2_noiseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_part2_noise" ---
for thisComponent in instructions_part2_noiseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-24.000000)

# set up handler to look after randomisation of conditions etc
noise_test = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CFMT/Test_noise.xlsx'),
    seed=None, name='noise_test')
thisExp.addLoop(noise_test)  # add the loop to the experiment
thisNoise_test = noise_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNoise_test.rgb)
if thisNoise_test != None:
    for paramName in thisNoise_test:
        exec('{} = thisNoise_test[paramName]'.format(paramName))

for thisNoise_test in noise_test:
    currentLoop = noise_test
    # abbreviate parameter names if possible (e.g. rgb = thisNoise_test.rgb)
    if thisNoise_test != None:
        for paramName in thisNoise_test:
            exec('{} = thisNoise_test[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Part2_noise" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Choices_5.setImage(noise)
    Answer_5.keys = []
    Answer_5.rt = []
    _Answer_5_allKeys = []
    noisnum.setText(nois_num)
    # keep track of which components have finished
    Part2_noiseComponents = [Answer_Prompt_5, Choices_5, Numbers_Test3_3, Answer_5, noisnum]
    for thisComponent in Part2_noiseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Part2_noise" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answer_Prompt_5* updates
        if Answer_Prompt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_Prompt_5.frameNStart = frameN  # exact frame index
            Answer_Prompt_5.tStart = t  # local t and not account for scr refresh
            Answer_Prompt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_Prompt_5, 'tStartRefresh')  # time at next scr refresh
            Answer_Prompt_5.setAutoDraw(True)
        
        # *Choices_5* updates
        if Choices_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choices_5.frameNStart = frameN  # exact frame index
            Choices_5.tStart = t  # local t and not account for scr refresh
            Choices_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choices_5, 'tStartRefresh')  # time at next scr refresh
            Choices_5.setAutoDraw(True)
        
        # *Numbers_Test3_3* updates
        if Numbers_Test3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Numbers_Test3_3.frameNStart = frameN  # exact frame index
            Numbers_Test3_3.tStart = t  # local t and not account for scr refresh
            Numbers_Test3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Numbers_Test3_3, 'tStartRefresh')  # time at next scr refresh
            Numbers_Test3_3.setAutoDraw(True)
        
        # *Answer_5* updates
        waitOnFlip = False
        if Answer_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_5.frameNStart = frameN  # exact frame index
            Answer_5.tStart = t  # local t and not account for scr refresh
            Answer_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_5, 'tStartRefresh')  # time at next scr refresh
            Answer_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Answer_5.status == STARTED and not waitOnFlip:
            theseKeys = Answer_5.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Answer_5_allKeys.extend(theseKeys)
            if len(_Answer_5_allKeys):
                Answer_5.keys = _Answer_5_allKeys[-1].name  # just the last key pressed
                Answer_5.rt = _Answer_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noisnum* updates
        if noisnum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noisnum.frameNStart = frameN  # exact frame index
            noisnum.tStart = t  # local t and not account for scr refresh
            noisnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noisnum, 'tStartRefresh')  # time at next scr refresh
            noisnum.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part2_noiseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Part2_noise" ---
    for thisComponent in Part2_noiseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer_5.keys in ['', [], None]:  # No response was made
        Answer_5.keys = None
    noise_test.addData('Answer_5.keys',Answer_5.keys)
    if Answer_5.keys != None:  # we had a response
        noise_test.addData('Answer_5.rt', Answer_5.rt)
    # the Routine "Part2_noise" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'noise_test'


# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
EndComponents = [text_8, key_resp_6]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
