import { ComponentStory, ComponentMeta } from '@storybook/react';
import { Loader } from './Loader';

export default {
    title: 'shared/Loader',
    component: Loader,
} as ComponentMeta<typeof Loader>;

const Template: ComponentStory<typeof Loader> = (args) => <Loader {...args} />;

export const Primary = Template.bind({});
Primary.args = {
    color: 'primary',
    size: 'xl',
};

export const Secondary = Template.bind({});
Secondary.args = {
    color: 'secondary',
    size: 'xl',
};

export const Accent = Template.bind({});
Accent.args = {
    color: 'accent',
    size: 'xl',
};

export const Soft = Template.bind({});
Soft.args = {
    color: 'soft',
    size: 'xl',
};

export const Disabled = Template.bind({});
Disabled.args = {
    color: 'disabled',
    size: 'xl',
};

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
