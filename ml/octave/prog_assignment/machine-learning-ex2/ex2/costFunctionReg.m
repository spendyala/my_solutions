function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

predictions = sigmoid(X*theta);
y_1_calc = -1 * y' * log(predictions);
y_0_calc = -1 * (1 - y') * log(1-predictions);

theta_zero = theta;
theta_zero(1) = 0; 

lambda_cost = (lambda/(2*m)) * sum(theta_zero .^2);
lambda_grad = (lambda/m) * theta_zero;


J = (y_1_calc + y_0_calc)/m + lambda_cost;

grad = (X' * (predictions - y))/m + lambda_grad;




% =============================================================

end
