# TouchDesigner Python — Copilot Instructions

> **Usage:** Copy this file to `.github/copilot-instructions.md` in any TouchDesigner project.
> Copilot loads it automatically for every chat in that workspace.

This workspace targets **TouchDesigner Python scripting**. Follow these conventions exactly.

## Object Model

TD Python runs inside TouchDesigner's embedded interpreter. Global objects are always available — never import them.

```python
# Pre-loaded globals — do NOT import these
td          # TouchDesigner module (td.run, td.absTime, etc.)
op          # Operator lookup function
me          # Current operator (context-dependent)
parent      # Parent component shortcuts
ui          # UI module (dialogs, status bar, etc.)
absTime     # Absolute time (frame, seconds, step)
```

### Operator References

```python
op('noise1')            # Relative path from current component
op('/project1/noise1')  # Absolute path
op('../noise1')         # Relative path navigation
parent()                # Parent COMP
parent.Shortcut         # Named parent shortcut (set on COMP)
me.ext.ClassName        # Extension on this or ancestor COMP
mod.datName             # Import a DAT as a Python module
```

## Parameter Access

Parameter names are **not guessable** — they use specific backtick identifiers from the docs (e.g., `roughness`, `resolutionw`, `outputresolution`). Always look up the correct identifier.

```python
# Reading
value = op('noise1').par.roughness.eval()   # Preferred — always works
value = op('noise1').par.roughness.val      # Equivalent to .eval()

# Setting
op('noise1').par.roughness = 0.5            # Direct assignment
op('noise1').par.roughness.val = 0.5        # Explicit value set
op('noise1').par.roughness.expr = 'me.time.seconds'  # Set expression

# Mode check
op('noise1').par.roughness.mode  # ParMode.CONSTANT or ParMode.EXPRESSION
```

## Operator Properties (Not Parameters)

```python
# Dimensions — these are OP properties, NOT par.*
op('noise1').width          # Pixel width (TOPs)
op('noise1').height         # Pixel height (TOPs)

# CHOP
op('constant1').numChans
op('constant1').numSamples
op('constant1')['chan1'].eval()

# DAT
op('table1').numRows
op('table1').numCols
op('table1')[0, 0].val         # Cell by row, col indices
op('table1')['row', 'col'].val # Cell by name
```

## Callback Signatures

These are the **exact** signatures. Do not invent parameters or change names.

### CHOP Execute DAT

```python
def onOffToOn(channel, sampleIndex, val, prev):
    return

def whileOn(channel, sampleIndex, val, prev):
    return

def onOnToOff(channel, sampleIndex, val, prev):
    return

def whileOff(channel, sampleIndex, val, prev):
    return

def onValueChange(channel, sampleIndex, val, prev):
    return
```

### DAT Execute DAT

```python
def onTableChange(dat):
    return

def onRowChange(dat, rows):
    return

def onColChange(dat, cols):
    return

def onCellChange(dat, cells, prev):
    return

def onSizeChange(dat):
    return
```

### Panel Execute DAT

```python
def onOffToOn(panelValue):
    return

def whileOn(panelValue):
    return

def onOnToOff(panelValue):
    return

def whileOff(panelValue):
    return

def onValueChange(panelValue):
    return
```

### OP Execute DAT

```python
def onPreCook(op):
    return

def onPostCook(op):
    return

def onDestroy(op):
    return

def onFlagChange(op, flag):
    return

def onNameChange(op):
    return

def onPathChange(op):
    return

def onNumChildrenChange(op):
    return

def onChildRename(op):
    return

def onCurrentChildChange(op):
    return

def onExtensionChange(op):
    return
```

## Rules

1. **No `import td`** — `td`, `op`, `me`, `parent`, `ui`, `absTime` are pre-loaded globals.
2. **No `op.par.width`** for dimensions — use `op.width` and `op.height` (operator properties).
3. **No invented parameter names** — always verify the backtick identifier from documentation.
4. **No threading with TD objects** — TouchDesigner is single-threaded for operator access.
5. **No `[row][col]`** for DAT cells — use `[row, col].val` (tuple indexing).
6. **`me` context varies** — in a Text DAT `me` is that DAT; in an Execute DAT callback `me` is the Execute DAT; in a parameter expression `me` is the operator owning the parameter.
7. **Pull-based cooking** — setting a parameter doesn't immediately trigger downstream evaluation.
8. **Coercion** — `par.Float1` is a Par object, not a number. Use `par.Float1.eval()` before math like `round()`.

## MCP Integration (Optional)

If [TD-MCP](https://github.com/cacheflowe/td-docs-mcp) is configured for this workspace, use its tools to verify parameter names and API details before writing `par.X` code:

- `search_touchdesigner_docs` — keyword search across all TD docs
- `read_operator_doc` — full documentation for a specific operator
- `get_python_class` — Python class API reference
