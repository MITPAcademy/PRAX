TEX_TEMPLATE = r"""
\documentclass[12pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{graphicx}}
\usepackage{{xcolor}}
\usepackage{{multicol}}
\usepackage{{fancyhdr}}
\usepackage{{titlesec}}
\usepackage{{enumitem}}
\usepackage{{tikz}}
\usepackage[most]{{tcolorbox}}
\definecolor{{mitred}}{{HTML}}{{D7261E}}
\definecolor{{mitblack}}{{HTML}}{{000000}}
\tcbset{{
  examquestion/.style={{
    width=\textwidth,
    colback=white,
    colframe=mitred,
    boxrule=0.8pt,
    arc=3pt,
    outer arc=3pt,
    left=2mm,
    right=2mm,
    top=2mm,
    bottom=2mm,
    boxsep=2pt,
    before skip=1em,
    after skip=2em,
    enhanced,
    breakable,
  }}
}}
\pagestyle{{empty}}
\begin{{document}}
\noindent
\begin{{minipage}}{{\textwidth}}
    \colorbox{{mitblack}}{{%
        \parbox[b][4em][c]{{\textwidth}}{{%
            \hspace{{0.5em}}%
            \includegraphics[height=3em]{{logo.png}}
        }}
    }}
\end{{minipage}}
\vspace{{3em}}
\noindent
\begin{{minipage}}[t]{{0.48\textwidth}}
    \raggedright
    \textbf{{Created At:}}\\
    {created_at}\\
    By: {creator}\\[6em]
    \textbf{{ID:}} {id}
\end{{minipage}}
\hfill
\begin{{minipage}}[t]{{0.48\textwidth}}
    \raggedleft
    \vspace{{2em}}
    {{\Huge \textbf{{{title}}}}}\\[0.5em]
    \Large \textbf{{{subtitle}}}
\end{{minipage}}
\vspace{{2em}}
\hrule
\vspace{{2em}}
{questions_latex}
\newpage
\noindent
\begin{{minipage}}{{\textwidth}}
    \colorbox{{mitblack}}{{%
        \parbox[b][4em][c]{{\textwidth}}{{%
            \hspace{{0.5em}}%
            \includegraphics[height=3em]{{logo.png}}
        }}
    }}
\end{{minipage}}
\vspace{{1em}}
\section*{{Answer Sheet}}
{answer_sheet_latex}
\end{{document}}
"""