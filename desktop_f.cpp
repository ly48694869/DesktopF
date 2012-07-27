
#ifdef X11
// 直接使用窗口接口库
#include <X11/Xlib.h> 
#include <GL/glx.h>
#elif
#include <GL/glut.h>

int main(int argc, char** argv){
	glInit
}
