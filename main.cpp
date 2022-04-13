#include "opencv2\opencv.hpp"

using namespace cv;

int main(int argv, char** argc)
{
	Mat test = imread("pixel_art.jpg", IMREAD_COLOR);

	imshow("Primeiro Teste",test);

	waitKey();

	return 0;
}