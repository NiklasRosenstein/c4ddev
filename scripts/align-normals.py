# This script aligns the normals of an object, trying to make them
# face outwards. The object should be fully closed and not
# self-intersecting.

import c4d
from c4dtools.misc import normalalign

def main():
  if not op or not op.CheckType(c4d.Opolygon):
    c4d.gui.MessageDialog("select a Polygon Object")
    return

  doc.StartUndo()
  doc.AddUndo(c4d.UNDOTYPE_CHANGE, op)
  doc.EndUndo()
  c4d.EventAdd()

  normalalign.align_object_normals(op)

if __name__ == '__main__':
  main()
