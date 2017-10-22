from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(420,420)
    glutCreateWindow("Flapping wings: CMS427, midterm exam, problem 4, page 2")
    glutDisplayFunc(renderScene)
    glutMainLoop()

def renderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSwapBuffers()

if __name__ == '__main__': main()