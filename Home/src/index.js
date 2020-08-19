import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './static/style'
import * as serviceWorker from './serviceWorker';

import { createStore, compose, applyMiddleware, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import thunk from 'redux-thunk'
import { authReducer } from './store/reducers/auth';

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const RootReducer = combineReducers({
  auth: authReducer,

})

const store = createStore(RootReducer, composeEnhances(applyMiddleware(thunk)))

const app = (
  <Provider store={store}>
    <App/>
  </Provider>
)
ReactDOM.render(app, document.getElementById('root'))

serviceWorker.unregister();
