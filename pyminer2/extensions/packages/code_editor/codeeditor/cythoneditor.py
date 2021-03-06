#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/9/7
@author:
@email:
@file: cythoneditor
@description: Code Editor
"""

__version__ = '0.1'

import logging
import os
import re
from PyQt5.Qsci import QsciLexer
from PyQt5.QtCore import QDir, QEvent, QObject, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox, QMenu, QAction, QShortcut
from pmgwidgets import CythonLexer
from yapf.yapflib import py3compat, yapf_api

# TODO to remove (use extensionlib)
from .baseeditor import PMBaseEditor, PMAPI

logger = logging.getLogger(__name__)


class PMCythonEditor(PMBaseEditor):
    """
    自定义编辑器控件
    """

    def __init__(self, parent=None):
        super(PMCythonEditor, self).__init__(parent, comment_string='#')
        self._extension_names.append('.pyx')
        self._init_editor()
        self._init_lexer(CythonLexer(self.textEdit))
        self._init_apis()
        self._init_actions()
        self._init_signals()
        # 编辑器主题
        self.slot_set_theme(self._theme)

        self.last_hint = ''

    def set_indicators(self, msgs, clear=True):
        """
        设置 error warning info 指示器

        :param msgs: 消息数组
        :param clear: 是否清空之前的标记
        :type msgs: Options[list, str]
        :type clear: bool
        :return:
        """
        pass

    def _init_actions(self) -> None:
        super()._init_actions()
        self._action_compile = QAction(self.tr('Compile to Library'), self.textEdit)
        self._action_analyse = QAction(self.tr('Analyse Profile'), self.textEdit)
        # self._shortcut_compile = QShortcut(Qt.Key_F1, self.textEdit)
        # self._action_compile.setShortcut(Qt.Key_F1)

    def _init_lexer(self, lexer: QsciLexer) -> None:
        """
        初始化语法解析器

        :return: None
        """
        super(PMCythonEditor, self)._init_lexer(lexer)

    def create_context_menu(self) -> 'QMenu':
        menu = super().create_context_menu()
        menu.addAction(self._action_compile)
        menu.addAction(self._action_analyse)
        return menu

    def _init_signals(self) -> None:
        """
        初始化信号绑定

        :return: None
        """
        super(PMCythonEditor, self)._init_signals()
        self._action_compile.triggered.connect(self.compile)
        self._action_analyse.triggered.connect(self.analyse)

    def get_hint(self):
        pos = self.textEdit.getCursorPosition()
        text = self.textEdit.text(pos[0])
        try:
            line = text[:pos[1] + 1]
        except Exception as e:
            logger.debug(e)
            line = ''
        hint: str = re.split(r'[;,:\./ \\!&\|\*\+\s\(\)\{\}\[\]]', line)[-1].strip()
        return hint

    def ends_with_dot(self):
        """
        判断光标左侧的代码是否以‘.’符号结束
        :return:
        """
        pos = self.textEdit.getCursorPosition()
        text = self.textEdit.text(pos[0])

        if text.strip() != '':
            return text.strip()[-1] == '.'
        return False

    def update_api(self, hint: str, pos: tuple):
        pass

    def set_api(self, api_list):
        self._apis = PMAPI(self._lexer)  # QsciAPIs(self._lexer)
        for s in api_list:
            self._apis.add(s)
        self._apis.prepare()

    def slot_text_changed(self) -> None:
        """
        内容变化槽函数

        :return: None
        """
        pos = self.textEdit.getCursorPosition()
        hint = self.get_hint()
        if (not hint.startswith(self.last_hint)) or self.last_hint == '':
            if not hint == '':
                if hint[-1] not in ('(', ')', '[', ']', '{', '}', '\'', '\:', ';', '/', '\\'):
                    self.update_api(hint, pos)
                else:
                    pass
            else:
                self.update_api(hint, pos)
        elif self.ends_with_dot():
            self.update_api(hint, pos)

        super(PMCythonEditor, self).slot_text_changed()

    def slot_about_close(self, save_all=False) -> QMessageBox.StandardButton:
        """
        是否需要关闭以及保存

        :param save_all: 当整个窗口关闭时增加是否全部关闭
        :return:QMessageBox.StandardButton
        """
        return super(PMCythonEditor, self).slot_about_close(save_all)

    def slot_code_format(self):
        """
        格式化代码
        注意，格式化之前需要保存光标的位置，格式化之后再将光标设置回当前的位置。
        :return:
        """
        pass

    def compile(self):
        """
        在终端中运行代码
        调用程序的进程管理接口。
        :return:
        """
        from pmgwidgets import run_command_in_terminal
        logger.warning('Running C Code is not supported for this Editor!')
        text = self.text().strip()
        if not text:
            return
        path = self._path
        import sys
        python_interpreter_path = sys.executable
        dir_name = os.path.dirname(path)
        setup_py_path = os.path.join(dir_name, 'setup.py')
        cmd = '%s %s build_ext --inplace' % (python_interpreter_path, setup_py_path)
        print(cmd)
        try:
            run_command_in_terminal(cmd)
        except Exception as e:
            logger.warning(str(e))

    def analyse(self):
        """
        在终端中运行代码
        调用程序的进程管理接口。
        :return:
        """
        from pmgwidgets import run_command_in_terminal
        logger.warning('Running C Code is not supported for this Editor!')
        text = self.text().strip()
        if not text:
            return
        path = self._path
        import sys
        python_interpreter_path = sys.executable
        dir_name = os.path.dirname(path)
        setup_py_path = os.path.join(dir_name, 'setup.py')
        cmd = '%s -m cython -a %s' % (python_interpreter_path, path)
        print(cmd)
        try:
            run_command_in_terminal(cmd)
        except Exception as e:
            logger.warning(str(e))

    def slot_code_run(self):
        """
        运行代码

        :return:
        """
        logger.warning('Running C Code is not supported for this Editor!')

    def slot_run_in_terminal(self):
        """
        在终端中运行代码
        调用程序的进程管理接口。
        :return:
        """
        logger.warning('Running C Code is not supported for this Editor!')
        text = self.text().strip()
        if not text:
            return
        path = self._path
        try:
            self._parent.run_python_file_in_terminal(path)
        except Exception as e:
            logger.warning(str(e))