import { ComponentStory, ComponentMeta } from '@storybook/react';
import { Loader } from './Loader';

export default {
    title: 'shared/Loader',
    component: Loader,
    argTypes: {
        backgroundColor: { control: 'color' },
    },
} as ComponentMeta<typeof Loader>;

const Template: ComponentStory<typeof Loader> = (args) => <Loader {...args} />;

export const XS = Template.bind({});
XS.args = {
    size: 'xs',
};

export const SM = Template.bind({});
SM.args = {
    size: 'sm',
};

export const MD = Template.bind({});
MD.args = {
    size: 'md',
};

export const LG = Template.bind({});
LG.args = {
    size: 'lg',
};

export const XL = Template.bind({});
XL.args = {
    size: 'xl',
};
